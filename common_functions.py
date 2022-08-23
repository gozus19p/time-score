import os
from datetime import datetime


def read_start_trace():
    return datetime.strptime(open('start-trace.txt', 'r').read(), '%Y-%m-%d %H:%M:%S.%f')


def update_git():
    os.system("git add . > /dev/null")
    os.system("git commit -m \"Aggiornamento bash;\" > /dev/null")
    os.system("git push > /dev/null")


class Difference:
    def __init__(self, difference_in_minutes, time_before):
        self.difference_in_minutes = difference_in_minutes
        self.time_before = time_before


def calculate_difference_in_minutes(issue_time, time_before, start_time):
    issue_datetime = datetime.strptime(issue_time, '%Y-%m-%d %H:%M:%S.%f')
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

    return Difference(difference_in_minutes=after_minutes - before_minutes, time_before=time_before)
