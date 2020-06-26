"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

time_spent_dict = {}

for row in calls:
    if row[0] not in time_spent_dict:
        time_spent_dict[row[0]] = int(row[3])
    else:
        time_spent_dict[row[0]] += int(row[3])
    
    if row[1] not in time_spent_dict:
        time_spent_dict[row[1]] = int(row[3])
    else:
        time_spent_dict[row[1]] += int(row[3])

number, total_time = max(time_spent_dict.items(), key=lambda x:x[1])
print(f"{number} spent the longest time, {total_time} seconds, on the phone during September 2016.")
