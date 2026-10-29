from records import student_managing

manager = student_managing()

menu = """
student records system
1. add student
2. list students
3. view student
4. update student
5. delete student
6. quit
"""

def theinput(x):
    value = input(f"{x}: ").strip()
    if not value:
        raise ValueError(f"{x} cannot be empty.")
    return value

def add_student():
    name = theinput("name")
    age = theinput("age")
    email = theinput("email")
    grade = theinput("grade")
    student_id = manager.create_student(name, age, email, grade)
    print(f"student created successfully. id: {student_id}")

def list_all_students():
    records = manager.list_students()

    if not records:
        print("no student records found.")
        return

    for student_id, record in records.items():
        print(
            f"id: {student_id} "
            f"name: {record['name']} "
            f"age: {record['age']} "
            f"email: {record['email']} "
            f"grade: {record['grade']}"
        )
         
def view_student():
    student_id = theinput("student id")
    record = manager.get_student(student_id)

    if record is None:
        return
    
    print(f"--- student details ---")
    print(f"id: {student_id}")
    print(f"name: {record['name']}")
    print(f"age: {record['age']}")
    print(f"email: {record['email']}")
    print(f"grade: {record['grade']}")

def edit_student():
    student_id = theinput("student id")

    record = manager.get_student(student_id)

    if record is None:
        return

    name = theinput("new name")
    age = theinput("new age")
    email = theinput("new email")
    grade = theinput("new grade")

    updated_record = manager.update_student(
        student_id,
        name=name,
        age=age,
        email=email,
        grade=grade
    )

    if updated_record is None:
        return

    print("updated successfully.")
    print(updated_record)


def remove_student():
    student_id = theinput("student id")

    confirmation = input(
        f"delete student {student_id}? (y/n): "
    )

    if confirmation == "y":
        manager.delete_student(student_id)
    else:
        print("cancelled.")


def main():
    actions = {
        "1": add_student,
        "2": list_all_students,
        "3": view_student,
        "4": edit_student,
        "5": remove_student
    }

    while True:
        print(menu)
        choice = input("choose an option: ")

        if choice == "6":
            print("goodbye")
            break

        if choice not in actions:
            print("invalid choice. please select 1 to 6.")
            continue
        
        actions[choice]()

        





if __name__ == "__main__":
    main()