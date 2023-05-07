import uuid

from data.db import get_cursor, commit_db

from exceptions import ModelNotFound

class Note:
    def __init__(self, cort, lab, pro, par) -> None:
        self.id = str(uuid.uuid4())

        """
        cursor = get_cursor()
        cursor.execute("INSERT INTO Student (id, name) VALUES (?, ?)", (self.id, self.name))
        cursor.close()
        """

        commit_db()
