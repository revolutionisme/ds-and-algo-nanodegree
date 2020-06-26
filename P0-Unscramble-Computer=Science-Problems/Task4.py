"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

non_spam_numbers = set()
for row in texts:
    non_spam_numbers.update([row[0], row[1]])

all_out_numbers = set()
for row in calls:
    all_out_numbers.add(row[0])
    non_spam_numbers.add(row[1])

potential_spam_numbers = list(all_out_numbers - non_spam_numbers)
potential_spam_numbers.sort()

print(f"These numbers could be telemarketers: ")
for number in potential_spam_numbers:
    print(number)
