class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

# Example usage:
students_list = [
    Student("TITAN", "22G347", 7.7),
    Student("Luffy", "L12AZ", 5.7),
    Student("Zoro", "Z789", 6.7),
    # Add more students as needed
]

sorted_students = sort_students(students_list)

# Display sorted students
for student in sorted_students:
    print(f"{student.name}, {student.roll_number}, CGPA: {student.cgpa}")
