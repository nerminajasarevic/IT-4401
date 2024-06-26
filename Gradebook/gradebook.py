# gradebook.py

# Display the average of each student's grade.
# Display the average for each assignment.

def calc_assignment_avg(gradebook):
    
    #number of students
    rows = len(gradebook)
    
    #number of assignments
    columns = len(gradebook[0])

    #divide sum of all grades for assignment by # of students
    assignment_avg = [sum(gradebook[row][col] for row in range(rows)) / rows for col in range(columns)]
    
    return assignment_avg

def calc_student_avg(gradebook):

    #divide sum of students grades by # of assignments
    student_avg = [sum(rows) / len(rows) for rows in gradebook]
    
    return student_avg

def display_results(assignment_avg, student_avg):
    
    print("Assignment Averages:")

    #iterate thru assignment avg list
    for i, avg in enumerate(assignment_avg):
        print(f"Assignment {i}: {avg:.2f}")
        
    print("\nStudent Averages:")

    #iterate thru student avg list
    for i, avg in enumerate(student_avg):
        print(f"Student {i}: {avg:.2f}")

gradebook = [[61, 74, 69, 62, 72, 66, 73, 65, 60, 63, 69, 63, 62, 61, 64],
             [73, 80, 78, 76, 76, 79, 75, 73, 76, 74, 77, 79, 76, 78, 72],
             [90, 92, 93, 92, 88, 93, 90, 95, 100, 99, 100, 91, 95, 99, 96],
             [96, 89, 94, 88, 100, 96, 93, 92, 94, 98, 90, 90, 92, 91, 94],
             [76, 76, 82, 78, 82, 76, 84, 82, 80, 82, 76, 86, 82, 84, 78],
             [93, 92, 89, 84, 91, 86, 84, 90, 95, 86, 88, 95, 88, 84, 89],
             [63, 66, 55, 67, 66, 68, 66, 56, 55, 62, 59, 67, 60, 70, 67],
             [86, 92, 93, 88, 90, 90, 91, 94, 90, 86, 93, 89, 94, 94, 92],
             [89, 80, 81, 89, 86, 86, 85, 80, 79, 90, 83, 85, 90, 79, 80],
             [99, 73, 86, 77, 87, 99, 71, 96, 81, 83, 71, 75, 91, 74, 72]]

#call calculate functions
assignment_avg = calc_assignment_avg(gradebook)
student_avg = calc_student_avg(gradebook)

#call display function
display_results(assignment_avg, student_avg)
