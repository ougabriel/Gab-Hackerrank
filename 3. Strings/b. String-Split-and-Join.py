# Splitting the string: The split() method breaks the input string into a list of 
# words based on whitespace.
# Joining the words: The '-'.join(words) method takes the list of words and joins 
# them into a single string, 
# with each word separated by a hyphen.

def split_and_join(line):
    
    words = line.split()
    result = "-".join(words)
    
    return result
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)




# In Python, a string can be split on a delimiter.
# Example:
# - "this is a string"
# >>> a = a.split("") # a is converted to a list of strings.
# >>> print a
# ['this',
# 'string']
# Joining a string is simple:
# "-".join(a)
# >>> print a
# this—a-stri ng

# Task
# (space) delimiter and join using a - hyphen.
# You are given a string. Split the string on a
# Function Description
# Complete the split_and_join function in the editor below.
# split_and_join has the following parameters:
# • string line: a string of space-separated words
# Returns
# • string: the resulting string
# Input Format
# The one line contains a string consisting of space separated words.
# Sample Input
# this is a string
# Sample Output
# this-is-a-string