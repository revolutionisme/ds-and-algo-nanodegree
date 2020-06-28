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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.
"""

area_codes = set()

def find_codes(number: str):
  if number.startswith("("):
    return number[number.find("(") + 1:number.find(")")]
  elif number.startswith("140"):
    return "140"
  elif " " in number and number.startswith(("7", "8", "9")):
    return number[:4]

for row in calls:
  if row[0].startswith("(080)"):
    area_codes.add(find_codes(row[1]))

code_list = list(area_codes)
code_list.sort()
print(f"The numbers called by people in Bangalore have codes:")
for code in code_list:
  print(code)

  
"""
Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

def is_fixed_line_bangalore(number):
  if number.startswith("(080)"):
    return True
  else:
    return False

fixed_to_fixed_count = 0
total_count = 0
for row in calls:
  if is_fixed_line_bangalore(row[0]):
    if is_fixed_line_bangalore(row[1]):
      fixed_to_fixed_count += 1
    total_count += 1

print(f"{fixed_to_fixed_count*100/total_count:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
