from .user import User
from .assigment import Assigment

from data.db import get_cursor, commit_db

from utils.exception import ModelNotFound


class Note:
    def __init__(self, student_id, assigment_id, note, court) -> None:
        cursor = get_cursor()
        self.note = note
        self.student_id = student_id
        self.assigment_id = assigment_id

        student = User.get_student_by_code(student_id)
        assigment = Assigment.get_assigment_by_id(assigment_id)

        if court == 1:
            query =  "INSERT INTO Note (court_1, student_id, assigment_id) VALUES (?, ?, ?)"
        
        elif court == 2:
            query =  "INSERT INTO Note (court_2, student_id, assigment_id) VALUES (?, ?, ?)"
        
        elif court == 3:
            query =  "INSERT INTO Note (court_3, student_id, assigment_id) VALUES (?, ?, ?)"

        else: raise Exception("Court not found")

        cursor.execute(query, (self.note, self.student_id, self.assigment_id))
        cursor.close()

        commit_db()


    @staticmethod
    def get_note(note_id):
        cursor = get_cursor()
        cursor.execute("SELECT * FROM Note WHERE id = ?", (note_id,))
        result = cursor.fetchone()

        if result: return result

        raise Exception("Note not found")


    @staticmethod
    def update_note(note_id, note, court):
        cursor = get_cursor()

        if court == 1:
            query =  "UPDATE Note SET court_1 = ? WHERE id = ?"
        
        elif court == 2:
            query =  "UPDATE Note SET court_2 = ? WHERE id = ?"
        
        elif court == 3:
            query =  "UPDATE Note SET court_3 = ? WHERE id = ?"

        cursor.execute(query, (note, note_id))

        result = cursor.fetchone()

        return result
