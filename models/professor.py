import uuid

from data.db import get_cursor, commit_db

from exceptions import ModelNotFound

class Professor:
    def __init__(self, name) -> None:
        self.id = str(uuid.uuid4())
        self.name = name

        cursor = get_cursor()
        cursor.execute("INSERT INTO Professor (id, name) VALUES (?, ?)", (self.id, self.name))
        cursor.close()

        commit_db()

    @staticmethod
    def get_professor(id):
        cursor = get_cursor()
        cursor.execute("SELECT * FROM Professor WHERE id = ?", (id,))
        result = cursor.fetchone()

        if result:
            return result

        return None
