# Why used file:

## What applied in the code of the OOP:

### Inheritance:
Between parent (`person`) and child (`student`), the student inherit from person class the name and age using `super()`

### Abstraction:
Used in person as a base class/template class using abstract method used as template that need to be done in every class that inherits from this class

### Encapsulation:
Did it in the student file in the grade attribute using 2 things: property/setter and double underscore (name mangling) so the access to change the grade value wouldnt be easy

#### More details about setter / __ in the code:

**Setter:**

I used setter to call the validator class (in validation.py file) that checks the grade to be between 0 and 100 even if i created after an object to change the grade number to be an out of bound value then it raises a valueError

**Property:**

To get / set the value without the need to call function but call it as attribute

`s.get_grade()` ---> `s.grade`

`s.set_grade(90)` ---> `s.grade(90)`

**Double underscore (`self.__grade`):**

Name mangling so the name changes internally to be the class name + the attribute name (`.student__grade`) so the access to it became harder

### Polymorphism:

Did it as an sepeareted part in polymorphism_easy_apply.py file where i am using the function of calculate_salary() in class named fulltime(), partttime() but each class it calculates the salary in different way

### Static methods:

Used in validation.py file used to combine all validation operations inside a single Class called validator, and we can use each function directly with the class name without creating a new Object each time

## Final summary:

In this project, i applied the main OOP concepts:

- **Inheritance:** to reuse attributes and methods from the parent class
- **Abstraction:** to define a template that child classes need to implement
- **Encapsulation:** to control access to attributes and validate values before changing them
- **Polymorphism:** to use the same function name with different implementations
- **Static methods:** to organize validation operations inside a class without needing to create an object