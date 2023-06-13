import datetime
import json
import os
import requests
import sys
import toml

import last_trace_handler

CONFIG = toml.load(os.path.join(os.path.dirname(__file__), "config.toml"))


def calculate_time(issue: str) -> str:
    """
    Calculate the time spent on the issue.
    :return: The time spent on the issue.
    """
    date_str = last_trace_handler.read_last_trace()
    last_trace_date = datetime.datetime.fromisoformat(date_str[0:23])

    # Check if the last trace is from today
    now = datetime.datetime.now()
    today_day = now.day == last_trace_date.day
    today_month = now.month == last_trace_date.month
    today_year = now.year == last_trace_date.year
    if not today_year or not today_month or not today_day:
        # If not, raise an exception
        print("Different days")
        raise Exception("Last trace is not from today. Please, write the first log of the day manually.")

    # Calculate the difference in minutes
    difference_in_minutes = int((now - last_trace_date).total_seconds() / 60)
    print(f"Total time working on [{issue.strip().upper()}]: {difference_in_minutes}m")
    return f"{difference_in_minutes}m"


def read_token() -> str:
    """
    Read the token from the file.
    :return: The token.
    """
    if not os.path.exists(os.path.join(os.path.dirname(__file__), "token.txt")):
        raise Exception(
            "Token file not found, please create a file named 'token.txt' in the same folder of this script.")
    with open(os.path.join(os.path.dirname(__file__), "token.txt"), "r") as token_file:
        return token_file.read().strip()


def log_time(issue: str, time: str, date: str, token: str, jira_url: str):
    """
    Log the time on the issue.
    :param issue: The issue.
    :param time: The time.
    :param date: The date.
    :param token: The token.
    :param jira_url: The url of the jira instance.
    """
    # Log the time
    url = jira_url.format(issue)
    date_formatted = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    print(f"Logging [{time}] of time spent on issue [{issue}] at [{date_formatted}]... ", end="")
    last_trace_handler.write_last_trace(date)

    response = requests.post(
        url=url,
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": token
        },
        data=json.dumps({
            "timeSpent": time,
            "comment": "Automatic log",
            "started": date
        })
    )
    if not f"{response.status_code}".startswith("2"):
        print(f"Error: {response.status_code} - {response.text}")
        raise Exception(f"Error logging time: {response.status_code} - {response.text}")
    print("Done")
    pass


def get_endpoint_url(endpoint_alias: str):
    """
    Get the endpoint url from the alias.
    :param endpoint_alias: The alias.
    :return: The url.
    """
    if endpoint_alias not in CONFIG:
        raise Exception(f"Endpoint '{endpoint_alias}' not found in the config file.")
    if "url" not in CONFIG[endpoint_alias]:
        raise Exception(f"Endpoint '{endpoint_alias}' does not have a 'url' field in the config file.")
    return CONFIG[endpoint_alias]["url"]


if __name__ == '__main__':

    error = False
    # Check arguments
    if len(sys.argv) < 2:
        print("Not enough arguments")
        error = True

    if len(sys.argv) > 5:
        print("Too many arguments")
        error = True

    if error:
        print("Usage: python jira-log.py <issue> [-t=<time>] [-e=<type>]")
        exit(1)

    type = "mipa"
    jira_url = None
    time = None
    issue = None
    for arg in sys.argv[1:]:
        if arg.strip().startswith("-e="):
            type = arg.strip().split("=")[1].strip().lower()
            jira_url = get_endpoint_url(type)
        if arg.strip().startswith("-t="):
            time = arg.strip().split("=")[1].strip().lower().replace("'", "").replace('"', "")
        if not arg.strip().startswith("-"):
            if issue is not None:
                print("Too many issues")
                print("Usage: python jira-log.py <issue> [-t=<time>] [-e=<type>]")
                exit(1)
            issue = arg.strip().upper()

    # If the time is provided by the user, use it, otherwise calculate it based on the last trace
    TIME = time if time is not None else calculate_time(issue)
    TOKEN = read_token()

    # Log the time
    date = f"{datetime.datetime.now().isoformat()[0:23]}+0000"
    log_time(issue, TIME, date, TOKEN, jira_url)
