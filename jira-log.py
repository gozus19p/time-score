import requests
import sys
import json
import datetime
import os

if len(sys.argv) != 4:
    print("Not enough arguments")
    exit(1)

jira = sys.argv[1]
issue = sys.argv[2].strip().upper()
time = sys.argv[3]
URL = f"https://jira.{jira}.it/jira/rest/api/2/issue/{issue}/worklog"

print(f"Logging [{time}] of time spent on issue [{issue}] (jira [{jira}])...")
date = f"{datetime.datetime.now().isoformat()[0:23]}+0000"

response = requests.post(
    url=URL,
    headers={
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Basic bWFudWVsLmdvenppQGNpbmVjYS5pdDpnckJPMjE/MTk5Nw=="
    },
    data=json.dumps({
        "timeSpent": time,
        "comment": "log",
        "started": date
    })
)
print(f"Response [{response.status_code}]")
# os.execl("score", issue)
