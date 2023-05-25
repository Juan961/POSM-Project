import uuid


from data.db import get_cursor, commit_db


class ProfessorNote:
    def __init__(self, student_code, assigment_name, note, court) -> None:
        if 0 < note > 5.0: raise Exception("Note not valid")
        if 1 < court > 3: raise Exception("Court not valid")

        self.student_code = student_code
        self.assigment_name = assigment_name
        self.note = note
        self.court = court

        note_exits = ProfessorNote.get_note(self.student_code, self.assigment_name)

        if note_exits:
            ProfessorNote.update_note(self.student_code, self.assigment_name, self.note, self.court)

        else:
            ProfessorNote.create_note(self.student_code, self.assigment_name, self.note, self.court)


    @staticmethod
    def get_note(student_code, assigment_name):
        cursor = get_cursor()
        cursor.execute("SELECT * FROM ProfessorNote WHERE student_code = ? AND assigment_name = ?", (student_code, assigment_name))
        result = cursor.fetchone()

        if result: return result

        return None


    @staticmethod
    def create_note(student_code, assigment_name, note, court):
        cursor = get_cursor()

        cursor.execute(f"INSERT INTO ProfessorNote (id, court_{court}, student_code, assigment_name) VALUES (?, ?, ?, ?)", (str(uuid.uuid4()), note, student_code, assigment_name))
        cursor.close()

        commit_db()

        return ProfessorNote.get_note(student_code, assigment_name)


    @staticmethod
    def update_note(student_code, assigment_name, note, court):
        cursor = get_cursor()

        cursor.execute(f"UPDATE ProfessorNote SET court_{court} = ? WHERE student_code = ? AND assigment_name = ?", (note, student_code, assigment_name))
        cursor.close()

        commit_db()

        return ProfessorNote.get_note(student_code, assigment_name)
