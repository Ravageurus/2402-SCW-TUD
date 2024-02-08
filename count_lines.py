"""
Aim;this is script counts the number of lines in standats input
Input: Strings from the command line
Output:name of the file
Author: E Andrusenko
"""
import sys

count =0
for line in sys.stdin:
	count += 1

print(count, "lines in the standart input")



