from data.db import get_cursor, commit_db

from utils.exception import ModelNotFound


class User:
    def __init__(self, code, name, role) -> None:
        self.code = code
        self.name = name

        if role != "STUDENT" and role != "PROFESSOR": raise Exception("User role not valid")

        self.role = role

        cursor = get_cursor()
        cursor.execute("INSERT INTO User (code, name, role) VALUES (?, ?, ?)", (self.code, self.name, self.role))
        cursor.close()

        commit_db()


    @staticmethod
    def get_student_by_code(code):
        cursor = get_cursor()
        cursor.execute("SELECT * FROM User WHERE code = ? AND role = 'STUDENT'", (code,))
        result = cursor.fetchone()

        if result: return result

        raise ModelNotFound("Student not found")


    @staticmethod
    def get_professor_by_code(code):
        cursor = get_cursor()
        cursor.execute("SELECT * FROM User WHERE code = ? AND role = 'PROFESSOR'", (code,))
        result = cursor.fetchone()

        if result: return result

        raise ModelNotFound("PROFESSOR not found")


    @staticmethod
    def add_student_assigment(assigment_id, user_id):
        cursor = get_cursor()
        cursor.execute("INSERT INTO StudentAssigment () values (?, ?, ?)", (assigment_id, user_id,))
        result = cursor.fetchone()

        if result: return result

        raise ModelNotFound("PROFESSOR not found")
