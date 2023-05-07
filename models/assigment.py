import uuid

from data.db import get_cursor, commit_db

from utils.exception import ModelNotFound

from .professor import Professor

class Assigment:
    def __init__(self, name, professor_id) -> None:
        self.id = str(uuid.uuid4())
        self.name = name
        self.professor_id = professor_id

        professor = Professor.get_professor(professor_id)

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

        if result:
            return result

        return None

    @staticmethod
    def get_all_assigments():
        cursor = get_cursor()

        cursor.execute("SELECT * FROM Assigment")
        rows = cursor.fetchall()
        cursor.close()

        return rows
