import datetime

# Writing start timestamp
now = datetime.datetime.now()
print(f"Starting to trace issue at {now}")
trace = open("start-trace.txt", "w")
trace.write(f"{now}")

# Resetting counter
counter_file = open("counter.txt", "w")
counter_file.write('0')


