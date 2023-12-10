#!/usr/bin/env python3

import re
def check_web_address(text):
  pattern = r"\w\.com$|\.org|\.US"
  result = re.search(pattern, text)
  return result != None

print(check_web_address(input("Enter the web address: "))