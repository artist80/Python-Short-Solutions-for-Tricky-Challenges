#!/usr/bin/env python3

import os

def create_python_script(filename):
	comments = "# Start of a new Python program"
	with open(filename, "w") as file:
		file.write(comments)
	filesize = os.path.getsize(filename)
	return filesize

print(create_pyton_script("anyname.py"))