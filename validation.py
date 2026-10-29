import re

class validator:
    @staticmethod
    def validate_name(name):
        name = name.strip()

        if not name:
            raise ValueError("name cannot be empty.")
        if not re.fullmatch(r"[a-zA-Z .'-]+", name):
            raise ValueError("invalid name.")
        return name

    @staticmethod
    def validate_age(age_str):
        try:
            age = int(age_str)
        except ValueError:
            raise ValueError("age must be a number.")

        if age < 5 or age > 120:
            raise ValueError("age must be between 5 and 120.")
        return age

    email_pattern = re.compile(r"^[\w.+-]+@[\w-]+\.[\w.-]+$")

    @staticmethod
    def validate_email(email):
        email = email.strip()
        if not validator.email_pattern.match(email):
            raise ValueError("invalid email.")
        return email

    @staticmethod
    def validate_grade(grade_str):
        try:
            grade = float(grade_str)
        except ValueError:
            raise ValueError("grade must be a number.")

        if grade < 0 or grade > 100:
            raise ValueError("grade must be between 0 and 100.")
        return grade