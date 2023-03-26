import uuid

from data import STUDENTS, PROFESSORS, ASSIGNEMETS

from .assigment import Assigment

class Student:
    def __init__(self, name) -> None:
        self.id = str(uuid.uuid4())

        self.name = name
        self.assigments = []

        STUDENTS.append(self)

    def __str__(self):
        return self.name

    @staticmethod
    def get_student(id):
        for student in STUDENTS:
            if student.id == id:
                return student 

        return None

    @staticmethod
    def get_all_students(id):
        return STUDENTS

    @staticmethod
    def add_asigment_to_user(student_id, assigment_id):
        student = Student.get_student(student_id)
        if not student: raise Exception("Student not found")

        assigment = Assigment.get_assigment(assigment)
        if not assigment: raise Exception("Assigment not found")

        student._add_asigment_to_user(assigment_id)

    def _add_asigment_to_user(self, assigment_id):
        self.assigments.append(assigment_id)
