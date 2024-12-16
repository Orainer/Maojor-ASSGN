class Course:
    def __init__(self, course_id, name, fee):
        self.course_id = course_id
        self.name = name
        self.fee = fee

class Student:
    def __init__(self, student_id, name, email):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.courses = []
        self.balance = 0.0

    def enroll(self, course):
        if course in self.courses:
            raise ValueError("Student is already enrolled in this course.")
        self.courses.append(course)
        self.balance += course.fee

    def get_total_fee(self):
        return sum(course.fee for course in self.courses)

class RegistrationSystem:
    def __init__(self):
        self.courses = []
        self.students = {}

    def add_course(self, course_id, name, fee):
        if any(course.course_id == course_id for course in self.courses):
            raise ValueError("Course ID already exists.")
        new_course = Course(course_id, name, fee)
        self.courses.append(new_course)

    def register_student(self, student_id, name, email):
        if student_id in self.students:
            raise ValueError("Student ID already exists.")
        new_student = Student(student_id, name, email)
        self.students[student_id] = new_student

    def enroll_in_course(self, student_id, course_id):
        if student_id not in self.students:
            raise ValueError("Student ID not found.")
        student = self.students[student_id]
        course = next((course for course in self.courses if course.course_id == course_id), None)
        if not course:
            raise ValueError("Course ID not found.")
        student.enroll(course)

    def calculate_payment(self, student_id, payment):
        if student_id not in self.students:
            raise ValueError("Student ID not found.")
        student = self.students[student_id]
        if payment < 0.4 * student.balance:
            raise ValueError("Payment must be at least 40% of the outstanding balance.")
        student.balance -= payment

    def check_student_balance(self, student_id):
        if student_id not in self.students:
            raise ValueError("Student ID not found.")
        student = self.students[student_id]
        return student.balance

    def show_courses(self):
        return [(course.course_id, course.name, course.fee) for course in self.courses]

    def show_registered_students(self):
        return [(student_id, student.name, student.email) for student_id, student in self.students.items()]

    def show_students_in_course(self, course_id):
        course = next((course for course in self.courses if course.course_id == course_id), None)
        if not course:
            raise ValueError("Course ID not found.")
        enrolled_students = [
            student.name for student in self.students.values() if course in student.courses
        ]
        return enrolled_students

def main():
    system = RegistrationSystem()


    while True:
        print("Menu:")
        print("1. Add Course")
        print("2. Register Student")
        print("3. Enroll Student in Course")
        print("4. Make Payment")
        print("5. Check Student Balance")
        print("6. Show All Courses")
        print("7. Show Registered Students")
        print("8. Show Students in a Course")
        print("9. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                course_id = input("Enter course ID: ")
                name = input("Enter course name: ")
                fee = float(input("Enter course fee: "))
                system.add_course(course_id, name, fee)
                print("Course added successfully.")

            elif choice == 2:
                student_id = input("Enter student ID: ")
                name = input("Enter student name: ")
                email = input("Enter student email: ")
                system.register_student(student_id, name, email)
                print("Student registered successfully.")

            elif choice == 3:
                student_id = input("Enter student ID: ")
                course_id = input("Enter course ID: ")
                system.enroll_in_course(student_id, course_id)
                print("Student enrolled in course successfully.")

            elif choice == 4:
                student_id = input("Enter student ID: ")
                payment = float(input("Enter payment amount: "))
                system.calculate_payment(student_id, payment)
                print("Payment processed successfully.")

            elif choice == 5:
                student_id = input("Enter student ID: ")
                balance = system.check_student_balance(student_id)
                print(f"Outstanding balance for student {student_id}: {balance}")

            elif choice == 6:
                courses = system.show_courses()
                print("Courses:")
                for course in courses:
                    print(f"ID: {course[0]}, Name: {course[1]}, Fee: {course[2]}")

            elif choice == 7:
                students = system.show_registered_students()
                print("Registered Students:")
                for student in students:
                    print(f"ID: {student[0]}, Name: {student[1]}, Email: {student[2]}")

            elif choice == 8:
                course_id = input("Enter course ID: ")
                students_in_course = system.show_students_in_course(course_id)
                print(f"Students in course {course_id}:")
                for student_name in students_in_course:
                    print(student_name)

            elif choice == 9:
                print("Exiting the system. Goodbye!")
                exit()

            else:
                print("Invalid choice. Please try again.")

        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()