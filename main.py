#!/usr/bin/env python3

import os
import datetime

def file_date(filename):
	# Create the file in the current directory
	with open(filename, "w") as file:
		pass

	# Get the current timestamp
	timestamp = os.path.gettime(filename)

	# Convert the timestamp into a readable format, then into a string
	date = datetime.datetime.fromtimestamp(timestamp).date()
	date_string = str(date)

	# Return just the date portion
	return date_string

print(file_date("newfile.txt"))
# Should be today's date in the format of yyyy-mm-dd