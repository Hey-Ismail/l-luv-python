# ----------#
# * Write a program that calculates and displays the average grade and the corresponding letter grade for multiple students

number_of_students = int(input("Enter the number of students: "))

# Initialize an empty list to store student data
students = []

# Loop to get details for each student
for i in range(number_of_students):
    print(f"\nStudent {i+1}:")
    name = input("Enter the student name: ")

    # Get the grades as a space-separated string and convert to a list of integers
    grades_input = input("Enter grades for three subjects separated by space: ")
    grades = [int(grade) for grade in grades_input.split()]

    # Calculate the average grade

    # total = sum(grades)  # Sum up all the grades
    # count = len(grades)  # Get the number of grades
    # average = total / count  # Calculate the average
    average = sum(grades) / len(grades)

    # Determine the letter grade
    if 90 <= average <= 100:
        letter_grade = "A+"
    elif 85 <= average < 90:
        letter_grade = "A"
    elif 80 <= average < 85:
        letter_grade = "B+"
    elif 75 <= average < 80:
        letter_grade = "B"
    elif 70 <= average < 75:
        letter_grade = "C+"
    elif 65 <= average < 70:
        letter_grade = "C"
    elif 60 <= average < 65:
        letter_grade = "D+"
    elif 50 <= average < 60:
        letter_grade = "D"
    else:
        letter_grade = "F"

    ## Store the student's details in a dictionary
    student = {
        "name": name,
        "grades": grades,
        "average": average,
        "letter_grade": letter_grade,
    }

    # Add the dictionary to the list of students
    students.append(student)

# Printing out the student information
print("\nStudents summary:")
for student in students:
    print(
        f"Name: {student['name']}, Grades: {student['grades']}, Average: {student['average']:.2f}, Letter Grade: {student['letter_grade']}"
    )
