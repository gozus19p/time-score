import datetime
import os

# Writing start timestamp
now = datetime.datetime.now()
print(f"Starting to trace issue at {now}")
trace = open("start-trace.txt", "w")
trace.write(f"{now}")

# Resetting counter
counter_file = open("counter.txt", "w")
counter_file.write('0')

# Issue
print("Clearing previous issues")
issues = os.listdir("issues/")
for issue in issues:
    file_name = f"issues/{issue}"
    os.remove(file_name)

