import uuid


from .user import User

from data.db import get_cursor, commit_db

from utils.exception import ModelNotFound


class Assigment:
    def __init__(self, name, professor_id) -> None:
        self.id = str(uuid.uuid4())
        self.name = name
        self.professor_id = professor_id

        professor = User.get_professor_by_code(professor_id)

        if not professor: raise ModelNotFound(f"Professor id: {professor_id}")

        cursor = get_cursor()
        cursor.execute("INSERT INTO Assigment (id, name, professor_id) VALUES (?, ?, ?)", (self.id, self.name, self.professor_id))
        cursor.close()

        commit_db()


    @staticmethod
    def get_assigment_by_id(id):
        cursor = get_cursor()
        cursor.execute("SELECT * FROM Assigment WHERE id = ?", (id,))
        result = cursor.fetchone()

        if result: return result

        raise Exception("Assigment not found")


    @staticmethod
    def get_all_assigments_by_professor_id():
        cursor = get_cursor()
        cursor.execute("SELECT * FROM Assigment")
        rows = cursor.fetchall()
        cursor.close()

        return rows


    @staticmethod
    def get_student_assigments(assigment_id, student_id):
        cursor = get_cursor()
        cursor.execute("SELECT * FROM StudentAssigment WHERE assigment_id = ? AND student_id = ?", (assigment_id, student_id))
        rows = cursor.fetchall()
        cursor.close()

        return rows


    @staticmethod
    def get_professor_assigments(professor_id):
        cursor = get_cursor()
        cursor.execute("SELECT * FROM Assigment WHERE professor_id = ?", (professor_id,))
        rows = cursor.fetchmany()

        return rows
