#!/usr/bin/env python3

import re
def check_time(text):
  pattern = r"^(1[0-2]|0?[1-9]):[0-5][0-9] ?(am|pm|AM|PM)$"
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False