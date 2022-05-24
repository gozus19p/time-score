import sys
import datetime

# Defining default formatting pattern
pattern = '%Y-%m-%d %H:%M:%S.%f'

# Reading issue code from arguments
issue_code = sys.argv[1]
actual_time = datetime.datetime.now()
print(f"Tracing issue [{issue_code}] at time [{actual_time}]")

# Opening counter file to read the current issue
counter_file = open("counter.txt", "r")
issue_prog = int(counter_file.read()) + 1
print(f"This is the #{issue_prog} issue of the day")

# Updating new counter
counter_file = open("counter.txt", "w")
if issue_prog < 10:
    counter_write = f"0{issue_prog}"
else:
    counter_write = f"{issue_prog}"

counter_file.write(f"{counter_write}")

# Opening new issue file
new_issue_file = open(f"issues/{counter_write}-{issue_code.lower()}.txt", "w")
new_issue_file.write(f"{actual_time}")

