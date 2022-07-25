import datetime
import os

directory_name = format(datetime.datetime.now(), '%Y-%m-%d')

start_time = datetime.datetime.strptime(open('start-trace.txt', 'r').read(), '%Y-%m-%d %H:%M:%S.%f')

# Capturing logged issues
logged_issues = os.listdir('issues')
logged_issues.sort()

worked_minutes = 0
time_before = None

for issue_file in logged_issues:

    # Copying file inside target directory
    opened_file = open(f'issues/{issue_file}', 'r')

    # Reading issue time
    issue_time = opened_file.read()
    issue_name = issue_file.replace(".txt", "")

    add_work_minutes = True
    if 'pausa' in str.lower(issue_name):
        add_work_minutes = False

    issue_datetime = datetime.datetime.strptime(issue_time, '%Y-%m-%d %H:%M:%S.%f')

    # Parsing the before date and time
    if time_before is not None:
        before_datetime = time_before
    else:
        before_datetime = start_time

    time_before = issue_datetime

    # Calculating total minutes before and after
    after_minutes = issue_datetime.hour * 60 + issue_datetime.minute
    before_minutes = before_datetime.hour * 60 + before_datetime.minute

    # Calculating difference in minutes
    difference_in_minutes = after_minutes - before_minutes

    if add_work_minutes:
        worked_minutes += difference_in_minutes

expected_worked_minutes = 60 * 8
total_minutes_left = expected_worked_minutes - worked_minutes

if total_minutes_left < 0:
    print("You are working extra hours. Go home buddy!")
else:
    hours_left = int(total_minutes_left / 60)
    minutes_left = total_minutes_left % 60
    print(f"Working time left: {hours_left}h, {minutes_left}m")

