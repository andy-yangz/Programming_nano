# Lesson 3.2: Use Functions
# Mini-Project: Secret Message

# Your friend has hidden your keys! To find out where they are,
# you have to remove all numbers from the files in a folder
# called prank. But this will be so tedious to do!
# Get Python to do it for you!

# Use this space to describe your approach to the problem.
#
#
#
#

# Your code here.
from os import listdir
from os.path import isfile, join
import os
def rename_files():
	file_list = listdir('./prank')
	saved_path = os.getcwd()
	os.chdir('./prank')
	for file_name in file_list:
		os.rename(file_name, file_name.translate(None,"0123456789"))
	os.chdir(saved_path)

rename_files()