import uuid

from data.db import get_cursor, commit_db

from utils.exception import ModelNotFound

from .assigment import Assigment

class Student:
    def __init__(self, name) -> None:
        self.id = str(uuid.uuid4())
        self.name = name

        cursor = get_cursor()
        cursor.execute("INSERT INTO Student (id, name) VALUES (?, ?)", (self.id, self.name))
        cursor.close()

        commit_db()


    @staticmethod
    def get_student_by_name(name):
        cursor = get_cursor()
        cursor.execute("SELECT * FROM Student WHERE name = ?", (name,))
        result = cursor.fetchone()

        if result: return result

        # raise ModelNotFound(f"{ name } student nor found")


    @staticmethod
    def get_student_by_id(id):
        cursor = get_cursor()
        cursor.execute("SELECT * FROM Student WHERE id = ?", (id,))
        result = cursor.fetchone()

        if result:
            return result

        # raise ModelNotFound(f"{ id } student nor found")


    @staticmethod
    def get_all_students():
        cursor = get_cursor()

        cursor.execute("SELECT * FROM Student")
        rows = cursor.fetchall()
        cursor.close()

        return rows


    @staticmethod
    def add_asigment_to_user(student_id, assigment_id):
        student = Student.get_student_by_id(student_id)
        if not student: raise ModelNotFound(f"Student id: {student_id}")

        assigment = Assigment.get_assigment(assigment_id)
        if not assigment: raise ModelNotFound(f"Assignment id: {assigment_id}")

        cursor = get_cursor()

        cursor.execute("INSERT INTO StudentAssigment (student_id, assigment_id) VALUES (?, ?)", (student_id, assigment_id))
        cursor.close()
