# Enter your code here. Read input from STDIN. Print output to STDOUT

N, M = map(int, input().split())  #insert input from STDIN
def print_doormat(N, M):
    
    #Top half
    for i in range(1, N, 2):   #starts at 1, ends at N and steps by 2
        print((i * '.|.').center(M, '-'))

    #Middle line
    print(('WELCOME').center(M, '-'))

    #bottom half
    for i in range(N-2, -1, -2):
        print((i * '.|.').center(M, '-'))
    

print_doormat(N, M)



# Mr. Vincent works in a door mat manufacturing company. One day, he designed a
# new door mat with the following specifications:
# • Mat size must be NXM. (N is an odd natural number, and M is 3 times N.)
# • The design should have 'WELCOME' written in the center.
# • The design pattern should only use l, . and - characters.


