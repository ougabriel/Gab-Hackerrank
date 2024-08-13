if __name__ == '__main__':
    n = int(input())
    arr = []
    
    for _ in range(n):
        command = input().split()
        action = command[0]
        
        if action == "insert":
            index = int(command[1])
            element = int(command[2])
            arr.insert(index, element)
        elif action == "print":
            print(arr)
        elif action == "remove":
            element = int(command[1])
            arr.remove(element)
        elif action == "append":
            element = int(command[1])
            arr.append(element)
        elif action == "sort":
            arr.sort()
        elif action == "pop":
            arr.pop()
        elif action == "reverse":
            arr.reverse()




# Consider a list (list = You can perform the following commands:
# 1. insert i e: Insert integer e at position i.
# 2. pri nt: Print the list.
# 3. remove e: Delete the first occurrence of integer e.
# 4. append e: Insert integer e at the end of the list.
# 5. sort: Sort the list.
# 6. pop: Pop the last element from the list.
# 7. reverse: Reverse the list.
# Initialize your list and read in the value of n followed by n lines of commands
# where each command will be of the 7 types listed above. Iterate through each
# command in order and perform the corresponding operation on your list.
# Example
# append 1
# append 2
# insert 3 1
# print
# • append 1: Append 1 to the list, arr
# • append 2: Append 2 to the list, arr
# • insert 3 1: Insert 3 at index 1, arr
# • print: Print the array.
