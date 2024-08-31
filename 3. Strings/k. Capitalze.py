#!/bin/python3

import math
import os
import random
import re
import sys
import math
import os
import random
import re
import sys
# Complete the solve function below.
def solve(s):

    return ' '.join([word.capitalize() for word in s.split(' ')])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()



###############################

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    # Split the string into words
    words = s.split(' ')  # Use space as the delimiter to split the string into words
    
    # Capitalize each word
    capitalized_words = [word.capitalize() for word in words]
    
    # Join capitalized words into a single string with spaces
    capitalized_string = ' '.join(capitalized_words)
    
    return capitalized_string

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()




################
#####TASK

# You are asked to ensure that the first and last names of people begin with a capital letter in their
# passports. For example, ati son heck should be capitalised correctly as Ali son Heck.
# lisom•ck
# Alison Hecl
# Given a full name, your task is to capitalize the name appropriately.
# Input Format
# A single line of input containing the full name, S.
# • ten(S) < 1000
# • The string consists of alphanumeric characters and spaces.
# Note in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.
# Output Format
# Print the capitalized string, S.
# Sarnple Input
# chris alan
# Sanvle Output
# Chris Alan