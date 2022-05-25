import os
import datetime

directory_name = format(datetime.datetime.now(), '%Y-%m-%d')

# Clearing the history of the day before
archive_subdirectories = os.listdir('archive')
directory_needs_to_be_created = not archive_subdirectories.__contains__(directory_name)

# Creating directory if needed
if directory_needs_to_be_created:
    print(f'Creating directory under archive for the day {directory_name}...')
    os.mkdir(f'archive/{directory_name}')

# Capturing logged issues
logged_issues = os.listdir('issues')
logged_issues.sort()

start_time = datetime.datetime.strptime(open('start-trace.txt', 'r').read(), '%Y-%m-%d %H:%M:%S.%f')

time_before = None
report = open(f'report/{directory_name}.csv', 'w')
report.write("Issue;Total time;\n")
for issue_file in logged_issues:

    # Copying file inside target directory
    opened_file = open(f'issues/{issue_file}', 'r')
    write_file = open(f'archive/{directory_name}/{issue_file}', 'w')

    # Reading issue time
    issue_time = opened_file.read()
    issue_name = issue_file.replace(".txt", "")
    write_file.write(issue_time)

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

    # Detecting hours and minutes
    hours_of_work = int(difference_in_minutes / 60)
    minutes = difference_in_minutes % 60

    issue_detail = issue_name.split("-")
    if len(issue_detail) == 3:
        report.write(f'{issue_detail[1].upper()}-{issue_detail[2]};{hours_of_work}h {minutes}m;\n')
    else:
        report.write(f'{issue_detail[1].upper()};{hours_of_work}h {minutes}m;\n')


os.system("git add . > /dev/null")
os.system("git commit -m \"Aggiornamento bash;\" > /dev/null")
os.system("git push > /dev/null")
os.system(f"libreoffice --calc report/{directory_name}.csv &")
print('Report has been generated successfully')

