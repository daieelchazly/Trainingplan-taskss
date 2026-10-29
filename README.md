# student records system

## overview of the student records system :
Implemantation command-line application of student records system that add , delete , list students in the json file , validation for (email , name , age , grade)
## features

- add a student with a name, age, email, and grade
- list all student records
- view a specific student
- update student information
- delete a student record
- validate user input
- save and load records using a json file
- run automated unit tests

## project structure

```text
student-records-cli/
├── main.py
├── student.py
├── records.py
├── saving_students.py
├── validation.py
├── students.json
├── tests/
│   └── test_student_records.py
└── README.md
```

## requirements

- python 3
- no additional packages are required for the current implementation

## how to run

1. open a terminal in the project directory.
2. activate the virtual environment if one is being used.
3. run the application:

```bash
python main.py
```

4. choose an option from the displayed menu.

## how to run the tests

run:

```bash
python -m unittest discover -s tests -v
```

the test runner displays the result of each test.

## data storage

student records are stored in `students.json`. the application loads the existing records and saves changes to this file.

## validation

the application validates student names, ages, email addresses, and grades before saving records.

## learning objectives

- practice python functions and classes
- understand inheritance and object-oriented programming
- implement crud operations
- handle json file storage
- validate user input
- write unit tests
- use git and github for version control
