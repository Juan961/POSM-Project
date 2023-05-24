import sqlite3


from data.db import get_cursor, commit_db

from .note import Note

from utils.exception import ModelNotFound, UserExists


class User:
    def __init__(self, code, name, role) -> None:
        try:
            self.code = code
            self.name = name

            if role != "STUDENT" and role != "PROFESSOR": raise Exception("User role not valid")

            self.role = role

            cursor = get_cursor()
            cursor.execute("INSERT INTO User (code, name, role) VALUES (?, ?, ?)", (self.code, self.name, self.role))
            cursor.close()

            commit_db()
        
        except sqlite3.IntegrityError as e:
            raise UserExists("Student is already in the db")


    @staticmethod
    def login(code):
        cursor = get_cursor()
        cursor.execute("SELECT * FROM User WHERE code = ?", (code,))
        result = cursor.fetchone()
        cursor.close()

        if not result: return None

        col_names = [desc[0] for desc in cursor.description]
        result_dict = {}
        for i in range(len(result)):
            result_dict[col_names[i]] = result[i]

        return result_dict


    @staticmethod
    def add_note(student_code, assigment_name, note, court):
        return Note(student_code, assigment_name, note, court)

    @staticmethod
    def get_student(student_code):
        cursor = get_cursor()
        cursor.execute('SELECT * FROM Note WHERE student_code = ?', (str(student_code),))

        result = cursor.fetchone()

        if not result: return None

        col_names = [desc[0] for desc in cursor.description]
        result_dict = {}
        for i in range(len(result)):
            result_dict[col_names[i]] = result[i]

        return result_dict


    @staticmethod
    def get_notes(student_code, assigment_name):
        user = User.get_student(student_code)

        if not user: return None, "student"

        cursor = get_cursor()
        cursor.execute("SELECT * FROM Note WHERE student_code = ? AND assigment_name = ?", (student_code, assigment_name))

        result = cursor.fetchone()

        if not result: return None, "note"

        col_names = [desc[0] for desc in cursor.description]
        result_dict = {}
        for i in range(len(result)):
            result_dict[col_names[i]] = result[i]

        return result_dict, None
