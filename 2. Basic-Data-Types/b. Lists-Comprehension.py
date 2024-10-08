if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    coordinates = [[i,j,k] for i in range(x + 1)
                            for j in range(y + 1)
                            for k in range(z + 1)
                            if i+j+k != n]
    print(coordinates)







# Let's learn about list comprehensions! You are given three integers c, y and z
# representing the dimensions of a cuboid along with an integer n. Print a list of all
# possible coordinates given by (i, j, k) on a 3D grid where the sum of i + j + k is
# not equal to n. Here, 0 i c; 0 j y; 0 < k < z. Please use list
# comprehensions rather than multiple loops, as a learning exercise.
# Example
# x = 1
# y = 1
# z = 2
# n = 3
# All permutations of [i, j, k] are:[[0,0,0],[0,0,1] etc]
# Print an array of the elements that do not sum to n =3.
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 0], [1, 0, 1], [0, 1, 1]]

# Input Format
# Four integers c, y, z and n, each on a separate line.
# Constraints
# Print the list in lexicographic increasing order.