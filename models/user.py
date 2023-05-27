import sqlite3


from data.db import get_cursor, commit_db

from .professorNote import ProfessorNote
from .studentNote import StudentNote

from utils.exception import UserExists


class User:
    def __init__(self, code, name, role) -> None:
        try:
            self.code = code
            self.name = name

            if role != "STUDENT" and role != "PROFESSOR": raise Exception("User role not valid")

            self.role = role

            cursor = get_cursor()
            cursor.execute("INSERT INTO User (code, name, role) VALUES (?, ?, ?)", (self.code, self.name, self.role))
            commit_db()
            cursor.close()
        
        except sqlite3.IntegrityError as e:
            raise UserExists("User is already in the db")


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
    def add_note_professor(student_code, assigment_name, note, court):
        return ProfessorNote(student_code, assigment_name, note, court)


    @staticmethod
    def add_note_student(student_code, assigment_name, note, court):
        return StudentNote(student_code, assigment_name, note, court)


    @staticmethod
    def get_user(user_code):
        cursor = get_cursor()
        cursor.execute('SELECT * FROM User WHERE code = ?', (str(user_code),))

        result = cursor.fetchone()

        cursor.close()

        if not result: return None

        col_names = [desc[0] for desc in cursor.description]
        result_dict = {}
        for i in range(len(result)):
            result_dict[col_names[i]] = result[i]

        return result_dict


    @staticmethod
    def get_notes(user_code, assigment_name, assigment_code):
        user = User.get_user(user_code)

        if not user: return None, "user"

        cursor = get_cursor()

        if user["role"] == "STUDENT":
            cursor.execute("SELECT * FROM StudentNote WHERE assigment_code = ? AND assigment_name = ?", (assigment_code, assigment_name))

        else:
            cursor.execute("SELECT * FROM ProfessorNote WHERE student_code = ? AND assigment_name = ?", (user_code, assigment_name))

        result = cursor.fetchone()

        cursor.close()

        if not result: return None, "note"

        col_names = [desc[0] for desc in cursor.description]
        result_dict = {}
        for i in range(len(result)):
            result_dict[col_names[i]] = result[i]

        return result_dict, None
