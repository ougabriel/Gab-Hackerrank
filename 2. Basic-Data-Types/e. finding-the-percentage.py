if __name__ == '__main__':
    students = {}
    n = int(input())
    
    for _ in range(n):
        student_input = input().split()
        names = student_input[0]
        marks = list(map(float, student_input[1:]))
        students[names] = marks
    
    query_name = input()
    query_marks = students[query_name]
    average_score = sum(query_marks)/len(query_marks)
    
    print(f"{average_score:.2f}")
    



#     Task
# The provided code stub is read in a dictionary containing key/value pairs of name:[Marks] for a list of students. Print the average of the marks array for the student name is provided, showing 2 places after the decimal.

# Example
# marks key: value pairs are

# ‘alpha’:[20, 30, 40]

# ‘beta’:[30, 50, 70]

# query_name = ‘beta’

 

# The query_name is ‘beta’. beta’s average score is (30 + 50 + 70)/3 = 50.0.

 
# Input Format
# The first line contains the integer n, the number of student records. The next n lines contain the names and marks obtained by a student, each value separated by a space. The final line contains query_name, the name of a student to query.

# Constraints
# 2 ≤ n ≤ 10
# 0 ≤ marks[i] ≤ 100
# length of the marks array = 3
# Output Format
# Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.