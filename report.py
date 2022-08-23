import datetime
import os

from common_functions import read_start_trace, update_git, calculate_difference_in_minutes
from report_functions import prepare_archive

now = datetime.datetime.now()
day_directory = format(now, '%Y-%m-%d')
month_directory = format(now, '%Y-%m')

prepare_archive(archive_name=month_directory, subdirectory_name=day_directory)

# Capturing logged issues
logged_issues = os.listdir('issues')
logged_issues.sort()

start_time = read_start_trace()

time_before = None
report = open(f'report/{month_directory}.csv', 'w')
report.write("Issue;Total time\n")

for issue_file in logged_issues:

    # Copying file inside target directory
    opened_file = open(f'issues/{issue_file}', 'r')
    write_file = open(f'archive/{month_directory}/{day_directory}/{issue_file}', 'w')

    # Reading issue time
    issue_time = opened_file.read()
    issue_name = issue_file.replace(".txt", "")
    write_file.write(issue_time)

    difference = calculate_difference_in_minutes(issue_time, time_before, start_time)
    time_before = difference.time_before

    # Detecting hours and minutes
    hours_of_work = int(difference.difference_in_minutes / 60)
    minutes = difference.difference_in_minutes % 60

    issue_detail = issue_name.split("-")
    if len(issue_detail) == 3:
        report.write(f'{issue_detail[1].upper()}-{issue_detail[2]};{hours_of_work}h {minutes}m\n')
    else:
        report.write(f'{issue_detail[1].upper()};{hours_of_work}h {minutes}m\n')

update_git()
os.system(f"libreoffice --calc report/{month_directory}.csv &")
print('Report has been generated successfully')
