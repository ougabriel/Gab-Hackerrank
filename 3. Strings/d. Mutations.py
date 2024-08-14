# This simple Python code snippet takes an immutable string, 
# converts it to a list, modifies it, and 
# then joins it back into a single string.

def mutate_string(string, position, character):
    i = list(string)
    i[position] = character
    string = "".join(i)
    
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


#Link: https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true

# Task
# Read a given string, change the character at a given index and then print the
# modified string.
# Function Description
# Complete the mutate_string function in the editor below.
# mutate_string has the following parameters:
# • string string: the string to change
# • int position: the index to insert the character at
# • string character: the character to insert
# Returns
# • string: the altered string
# Input Format
# The first line contains a string, string.
# The next line contains an integer position, the index location and a string
# character, separated by a space.
# Sample Input
# STDIN
# abracadabra
# Sample Output
# abrackdabra
