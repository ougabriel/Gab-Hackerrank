if __name__ == '__main__':
    students = []
    n = int(input())

    for _ in range(n):
        name = (input())
        score = float(input())
        students.append([name,score])

    scores = [student[1] for student in students]

    unique_scores = sorted(set(scores))
    second_lowest_score = unique_scores[1]
    
    names = [student[0] for student in students if student[1] == second_lowest_score]

    names.sort()
    for name in names:
        print(name)






#1. Initialize an empty list
#2. Recieve an input entry for number of students
#3. for each student loop N times
    # - Input the student's `name`.
    # - Input the student's `score`.
    # - Append `[name, score]` to the `students` list.
#4. Extract all scores from students
    # - create a list `scores` containing only scores of the students
#5. Find the lowest-second score
    # - Convert `scores` to a set to remove duplicates.
    # - Sort the unique scores.
    # - Identify the second-lowest score as the second element in the sorted list.
#6. Identify student with the second lowest score
    # - Initialize an empty list `names`.
    # - Loop through `students` and append the name of any student whose score matches the second-lowest score to `names`.
#7. sort the names list alphabetically
#8. Print each name in names on a new line






# Given the names and grades for each student in a class of N students, store them
# in a nested list and print the name(s) of any student(s) having the second lowest
# grade.
# Note: If there are multiple students with the second lowest grade, order their
# names alphabetically and print each name on a new line.
# Example
# — [["chi" , 20.0], ["beta" , 50.0], alpha" , 50.0]]
# records —
# The ordered list of scores is [20.0, 50.0], so the second lowest score is 50.0. There
# are two students with that score: ["beta" , " alpha"]. Ordered alphabetically, the
# names are printed as:
# alpha
# beta
# Input Format
# The first line contains an integer, N, the number of students.
# The 2N subsequent lines describe each student over 2 lines.
# - The first line contains a student's name.
# - The second line contains their grade.
# Constraints
# • There will always be one or more students having the second lowest grade.