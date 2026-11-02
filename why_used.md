# OOP Implementation Summary

## 1. Why Did We Use Separate Files?

We divided the code into separate files to organize the project and make the code easier to maintain and reuse.

Each file has a specific responsibility:
- `student.py`: Contains the `person` and `student` classes.
- `validation.py`: Contains the `validator` class and its validation methods.
- `polymorphism_easy_apply.py`: Demonstrates the implementation of polymorphism using different salary calculations.

## 2. What OOP Concepts Were Applied in the Code?

### 1. Inheritance

Implemented between the parent class `person` and the child class `student`.

The `student` class inherits the `name` and `age` attributes from the `person` class using `super().__init__(name, age)`.

This allows the child class to reuse the parent's attributes and methods without rewriting them.

### 2. Abstraction

Implemented in the `person` class by making it an abstract base class using `ABC`.

An abstract method, `display_info()`, was defined using `@abstractmethod`.

This acts as a template that requires every non-abstract child class to implement the `display_info()` method before its objects can be created.

### 3. Encapsulation

Implemented in the `student` class through the `grade` attribute using two main techniques:

- `@property` and `@grade.setter`
- Double underscore (`__`), also known as name mangling.

These techniques help control access to the grade attribute and validate its value before updating it.

#### More Details About Setter and Double Underscore

**A. Setter**

I used the setter to call the `validator` class from `validation.py`.

It checks that the grade is between 0 and 100, even if I try to change the grade after creating a student object.

If the new grade is outside this range, the validator raises a `ValueError`.

**B. Property**

The `@property` decorator allows me to access a method like an attribute, without explicitly calling it as a function.

For example:

- Instead of `s.get_grade()`, I can use `s.grade` to get the value.
- Instead of `s.set_grade(90)`, I can use `s.grade = 90` to update the value.

**C. Double Underscore (`self.__grade`)**

This is known as **Name Mangling**.

Python internally changes the attribute name by adding the class name as a prefix.

For example, inside the `student` class:

`self.__grade` becomes `_student__grade` internally.

This makes direct access to the attribute harder and helps prevent accidental access or modification. It is not a strict security mechanism.

### 4. Polymorphism

Implemented separately in `polymorphism_easy_apply.py`.

I used a method called `calculate_salary()` in two different classes:

- `fulltime`
- `parttime`

Both classes have the same method name, but each class implements it differently to calculate the salary according to its own rules.

This demonstrates polymorphism: the same method name can have different behaviors depending on the object.

### 5. Static Methods

Implemented in `validation.py`.

I used `@staticmethod` to combine all validation operations inside a single class called `validator`.

Each validation method checks a specific value, such as a name, age, email, or grade.

Since these methods do not need access to a specific object (`self`) or class data (`cls`), they are defined as static methods.

This allows me to call each method directly using the class name without creating a new object every time.

For example:

```python
validator.validate_age(20)
validator.validate_grade(90)
validator.validate_name("Daie")
```

## 3. Final Summary

The project demonstrates the main OOP concepts:

- **Inheritance:** Reusing attributes and methods from a parent class.
- **Abstraction:** Defining a template that child classes must implement.
- **Encapsulation:** Controlling access to data and validating values before updating them.
- **Polymorphism:** Using the same method name with different implementations.
- **Static Methods:** Organizing independent operations inside a class without requiring an object.