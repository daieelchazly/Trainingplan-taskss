from student import student
from saving_students import load_records, save_records
from validation import validator

class student_managing:
    def create_student(self, name, age, email, grade):
        records = load_records()
        
        if records:
            student_id = str(max(map(int, records)) + 1)
        else:
            student_id = "1"

        new_student = student( student_id,
            validator.validate_name(name),
            validator.validate_age(age),
            validator.validate_grade(grade)
        )

        validated_email = validator.validate_email(email)

        records[student_id] = {
            "name": new_student.name,
            "age": new_student.age,
            "email": validated_email,
            "grade": new_student.grade
        }

        save_records(records)
        return student_id

    def list_students(self):
        return load_records()

    def get_student(self, student_id):
        records = load_records()

        if student_id not in records:
            print("student not found.")
            return None

        return records[student_id]

    def update_student(self, student_id, **fields):
        records = load_records()

        if student_id not in records:
            print("student not found.")
            return None

        record = records[student_id]

        if "name" in fields:
            record["name"] = validator.validate_name(fields["name"])
        if "age" in fields:
            record["age"] = validator.validate_age(fields["age"])
        if "email" in fields:
            record["email"] = validator.validate_email(fields["email"])
        if "grade" in fields:
            record["grade"] = validator.validate_grade(fields["grade"])

        save_records(records)
        return record

    def delete_student(self, student_id):

        records = load_records()

        if student_id not in records:
            print("student not found.")
            return

        del records[student_id]
        save_records(records)