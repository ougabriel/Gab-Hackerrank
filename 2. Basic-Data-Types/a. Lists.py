if __name__ == '__main__':
    n = int(input())
    student_scores = {}
    
    for _ in range(n):
        name, *allmarks = input().split()
        marks = list(map(float, allmarks))
        
        student_scores[name] = marks
         
    query_name = input()
    marks = student_scores[query_name]
    
    average = sum(marks)/len(marks)
    print(f"{average:.2f}")


    ##########################################

    if __name__ == '__main__':
    # Read the number of student records
    n = int(input())

    # Initialize an empty dictionary to store student records
    student_marks = {}

    # Loop over the number of students
    for _ in range(n):
        # Read the student name and their marks
        # The *allmarks captures the rest of the input as a list
        name, *allmarks = input().split()

        # Convert the marks from strings to floats
        scores = list(map(float, allmarks))

        # Store the student's name and their marks in the dictionary
        student_marks[name] = scores

    # Read the name of the student to query
    query_name = input()

    # Retrieve the marks for the queried student from the dictionary
    scores = student_marks[query_name]

    # Calculate the average of the marks
    average = sum(scores) / len(scores)

    # Print the average rounded to 2 decimal places
    print(f'{average:.2f}')









# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided. showing 2 places after the decimal.
# Example
# marks key:value pairs are
# 'alpha': [20, 30, 40]
# 'beta': [30, 50, 70]
# query—name = 'beta'
# The query—name is 'beta'. beta's average score is (30 + 50-4-70)/3 = 50.0
# Input Format
# The first line contains the integer n. the number of students' records. The next n lines contain the names and marks obtained by a student. each value separated by a space. The final line contains query name. the name of a student to query.
# Constraints
# • 0 marks[il 100
# • length of marks arrays = 3
# Output Format
# Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.
# Sample Input O
# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika
# Sample Output O
# 56.00
# Explanation O

# Marks for Malika are {52, 56, 60} whose average is
# 52+56+60/3  = 56
# Sample Input 1
# 2
# Harsh 25 26.5 28
# Anurag 26 28 30
# Harsh

# Sample Output 1
# 26.50