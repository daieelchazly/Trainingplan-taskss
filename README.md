# student records cli system

a command-line interface (cli) application built with python for managing student records

## features

- **complete crud operations:** create, read, update, delete, and list student records
- **data persistence:** saves and loads records using local json storage (`students.json`)
- **robust validation:** input validation to prevent empty fields, invalid emails, and incorrect data types
- **automated testing:** fully tested using `pytest` with 8+ comprehensive unit test cases 

## project structure

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
```
## Installation & Setup

1. **Clone the repository:**

   ```bash
   git clone <your-repository-url>
   cd student-records-cli
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv .venv
   ```
   
3. **Install dependencies:**
   ```bash
   pip install pytest
   ```

## 🎮 How to Run the Application

Run the main CLI script from your terminal:

```bash
python main.py
```

Follow the interactive numbered menu (1 to 6) to manage student records smoothly.

## 🧪 Running Unit Tests

To run the test suite and verify the application's functionalities and validation rules, execute:

```bash
pytest
```