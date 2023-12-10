#!/usr/bin/env python3

import re
def check_time(text):
  pattern = r"^(1[0-2]|0?[1-9]):[0-5][0-9] ?(am|pm|AM|PM)$"
  result = re.search(pattern, text)
  return result != None

print(check_time(input("Enter the time and we will check whether you enter right time or not: ")))