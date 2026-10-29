# Student records cli system

a command-line interface (cli) application built with python for managing student records

## Features

- **complete crud operations:** create, read, update, delete, and list student records
- **data persistence:** saves and loads records using local json storage (`students.json`)
- **robust validation:** input validation to prevent empty fields, invalid emails, and incorrect data types
- **automated testing:** fully tested using `pytest` with 8+ comprehensive unit test cases 

## Project structure

```text
student-records-cli/
│
├── main.py             # user interface, menu options, and input handling (CLI)
├── records.py          # student management, and CRUD operations
├── student.py          # classes definition (Person and Student using OOP)
├── validation.py       # input validation rules (name, age, email, grade)
├── saving_students.py  # handles reading and writing data to the JSON file
├── students.json       # Local data storage file
├── test_records.py     # Pytest unit tests suite (8+ tests)
`