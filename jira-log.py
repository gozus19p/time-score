import datetime
import json
import os
import sys

import requests


def calculate_time(issue: str) -> str:
    """
    Calculate the time spent on the issue.
    :return: The time spent on the issue.
    """
    with open(os.path.join(os.path.dirname(__file__), "last-trace.txt"), "r") as f:
        date_str = f.read()
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


def log_time(issue: str, time: str, date: str, token: str):
    """
    Log the time on the issue.
    :param issue: The issue.
    :param time: The time.
    :param date: The date.
    :param token: The token.
    """
    # Log the time
    url = f"https://jira-mipa.cineca.it/jira/rest/api/2/issue/{issue}/worklog"
    date_formatted = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    print(f"Logging [{time}] of time spent on issue [{issue}] at [{date_formatted}]... ", end="")
    with open(os.path.join(os.path.dirname(__file__), "last-trace.txt"), "w") as last_trace:
        last_trace.write(date)

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


if __name__ == '__main__':
    # Check arguments
    if len(sys.argv) != 2 and len(sys.argv) != 3:
        print("Not enough arguments")
        exit(1)

    # Get issue and time
    ISSUE = sys.argv[1].strip().upper()

    # If the time is provided by the user, use it, otherwise calculate it based on the last trace
    TIME = sys.argv[2] if len(sys.argv) == 3 else calculate_time(ISSUE)
    TOKEN = read_token()

    # Log the time
    date = f"{datetime.datetime.now().isoformat()[0:23]}+0000"
    log_time(ISSUE, TIME, date, TOKEN)
