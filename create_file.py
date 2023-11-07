#!/usr/bin/env python3

import os
import sys

filename=sys.argv9[1]

if not os.path.exists(filename):
	with open(filename, "w") as f:
		f.write("New file create\n")
else:
	print("Error, the file {} already exists!".format(filename))
	sys.exit(1)