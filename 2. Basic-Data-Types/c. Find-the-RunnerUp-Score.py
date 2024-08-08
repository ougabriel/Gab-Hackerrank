
#########
# Read the input values.
# Store the scores in a list.
# Find the highest score.
# Remove all instances of the highest score from the list using list comprehension
# Find the highest score from the remaining list, which will be the runner-up score.
# Print the runner-up score.



if __name__ == '__main__':
    n = int(input())
    scores = list(map(int, input().split()))

    highest_score = max(scores)

    scores = [score for score in scores if score != highest_score]
    runner_up = max(scores)

    print(runner_up)

























# Given the participants' score sheet for your University Sports Day, you are required
# to find the runner-up score. You are given n scores. Store them in a list and find
# the score of the runner-up.
# Input Format
# The first line contains n. The second line contains an array ] of n integers each
# separated by a space.
# Constraints
# 2 <= n <= 10
# -100 <=  A[i] <= 100
# Output Format
# Print the runner-up score.
# Sample Input O
# 5
# 23665
# Sample Output O
# 5
# Explanation O
# Given list is [2, 3, 6, 6, 5]. The maximum score is 6, second maximum is 5. Hence,
# we print 5 as the runner-up score.