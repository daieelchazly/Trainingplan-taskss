
import pytest
from records import student_managing


@pytest.fixture
def manager():
    return student_managing()


def test_create_student(manager):
    student_id = manager.create_student(
        "Ali", 22, "ali@gmail.com", 90
    )
    assert manager.get_student(student_id)["name"] == "Ali"


def test_student_missing(manager):
    assert manager.get_student("33") is None


def test_listing(manager):
    manager.create_student("mariam", 20, "mariam@gmail.com", 85)
    assert len(manager.list_students()) > 0


def test_updating(manager):
    student_id = manager.create_student(
        "mohammed", 25, "mohammed@gmail.com", 80)

    updated = manager.update_student(student_id, name="mohammed Ali")
    assert updated["name"] == "mohammed Ali"


def test_deletion(manager):
    student_id = manager.create_student(
        "Mona", 21, "mona@gmail.com", 75)
    
    manager.delete_student(student_id)
    assert manager.get_student(student_id) is None


def test_empty_name(manager):
    with pytest.raises(ValueError):
        manager.create_student("", 22, "daie@gmail.com", 90)


def test_invalid_age(manager):
    with pytest.raises(ValueError):
        manager.create_student(
            "daie", "me", "daie@gmail.com", 90
        )


def test_invalid_email(manager):
    with pytest.raises(ValueError):
        manager.create_student(
            "daie", 22, "yy", 90
        )
