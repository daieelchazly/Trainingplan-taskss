
from abc import ABC, abstractmethod
from validation import validator

class person(ABC):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def display_info(self):
        pass


class student(person):

    def __init__(self, student_id, name, age, grade):
        super().__init__(name, age)
        self.student_id = student_id
        self.grade = grade

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, value):
        self.__grade = validator.validate_grade(value)

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

    def student_info(self):
        self.display_info()
        print(f"ID: {self.student_id}")
        print(f"Grade: {self.grade}")

s = student(101, "Daie", 21, 90)


s.display_info()

s.student_info()