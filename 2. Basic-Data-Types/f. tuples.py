# 1. An input integer `n`
# 2. An input integer `n` with spaces
# 3. Tuple creation (converting integer_list to tuple)
# 4. Calling the hash function for the tuple
# 5. output of the hash function

if __name__ == '__main__':
    n = int(input()) 
   
    integer_list = map(int, input().split())
    t = tuple(interger_list)
    result = hash(t)
    
    print(result)

##or
##another way
####################################concise way


if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    print(hash(tuple(integer_list)))


# Task
# Given an integer, n, and n space-separated integers as input, create a tuple, t, of those n
# integers. Then compute and print the result of hash(t).
# Note: hash() is one of the functions in the _ _ bui Iti ns__ module, so it need not be
# imported.
# Input Format
# The first line contains an integer, n, denoting the number of elements in the tuple.
# The second line contains n space-separated integers describing the elements in tuple t.
# Output Format
# Print the result of hash(t).
# Sample Input O
# 2
# 12
# Sample Output O
# 3713081631934410656