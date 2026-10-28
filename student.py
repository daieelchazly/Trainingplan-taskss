
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class student(person):
    def __init__(self, student_id, name, age, grade):
        super().__init__(name, age)
        self.student_id = student_id
        self.grade = grade

    def student_info(self):
        self.display_info()
        print(f"ID: {self.student_id}")
        print(f"Grade: {self.grade}")
