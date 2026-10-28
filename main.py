
from student import Student
def main():
    student1 = Student(1, "Daie", 20, 90)
    student2 = Student(2, "Ali", 21, 85)

    print("welcome to Student Records system")

    student1.student_info()
    student2.student_info()


if __name__ == "__main__":
    main()
