#!/usr/bin/env python3

import os

def new_directory(directory, filename):
	# Before creating a new directoy, check to if it already exists
	if not os.path.isdir(directory)

	# Create the new file inside the new directory
	os.chdir(directory)
	with open(filename, "w") as file:
		pass

	# Return the list of files in the new directory
	file_list = os.listdir()
	return file_list

print(new_directory("PythonPrograms", "script.py"))