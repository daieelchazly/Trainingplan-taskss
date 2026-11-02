# OOP implementation summary

## 1. why did we use separate files?

We split the code into separate files to organize the code and make it easy to reuse and maintain.

Files' responsibilities are as follows:
- `student.py` - file which includes `person` and `student` classes.
- `validation.py` - file which includes `validator` class and its validation methods.
- `polymorphism_easy_apply.py` - demonstrates implementation of polymorphism through the usage of different salary calculations.

## 2. what OOP concepts were applied in the code?

### 1. inheritance

Implemented between the parent `person` class and child `student` class.

Child class uses `super().__init__(name, age)` to inherit attributes `name` and `age` from parent class.

This allows the child class to reuse the attributes and methods of the parent class without rewriting them.

### 2. abstraction

Implemented in `person` class through marking it as an abstract base class with the use of `ABC`.

Abstract method `display_info()` was implemented using `@abstractmethod`.

Abstract method is a template for child classes which requires them to implement this method before creating objects.

### 3. encapsulation

Implemented in `student` class through the use of `grade` attribute in two ways:

- @property and @grade.setter
- Double underscore (`__`), also known