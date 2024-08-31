import string

def print_rangoli(size):
    # Create a string of lowercase alphabets
    alpha = string.ascii_lowercase
    
    # Create an empty list to hold each row of the rangoli
    L = []
    
    # Generate the pattern row by row
    for i in range(size):
        # Create the row string by joining characters with a hyphen
        s = '-'.join(alpha[size-1:i:-1] + alpha[i:size])
        # Center the string within a width of 4*size - 3
        L.append(s.center(4*size - 3, '-'))
    
    # Print the complete rangoli by joining the list `L`
    print('\n'.join(L[::-1] + L[1:]))



if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)