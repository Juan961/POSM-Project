import sqlite3


from data.db import get_cursor, commit_db

from utils.exception import UserExists


class Assigment:
    def __init__(self, code, name) -> None:
        try:
            self.code = code
            self.name = name
            cursor = get_cursor()
            cursor.execute("INSERT INTO Assigment (code, name) VALUES (?, ?)", (self.code, self.name))
            commit_db()
            cursor.close()

        except sqlite3.IntegrityError as e:
            raise UserExists("Student is already in the db")


    @staticmethod
    def get_assigmet(assigment_code):
        cursor = get_cursor()
        cursor.execute('SELECT * FROM Assigment WHERE code = ?', (str(assigment_code),))
        result = cursor.fetchone()
        cursor.close()

        if not result: return None

        col_names = [desc[0] for desc in cursor.description]
        result_dict = {}
        for i in range(len(result)):
            result_dict[col_names[i]] = result[i]

        return result_dict
