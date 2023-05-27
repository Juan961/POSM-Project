import uuid


from data.db import get_cursor, commit_db


class StudentNote:
    def __init__(self, assigment_code, assigment_name, note, court) -> None:
        if 0 < note > 5.0: raise Exception("Note not valid")
        if 1 < court > 3: raise Exception("Court not valid")

        self.student_code = assigment_code
        self.assigment_name = assigment_name
        self.note = note
        self.court = court

        note_exits = StudentNote.get_note(self.assigment_code, self.assigment_name)

        if note_exits:
            StudentNote.update_note(self.assigment_code, self.assigment_name, self.note, self.court)

        else:
            StudentNote.create_note(self.assigment_code, self.assigment_name, self.note, self.court)


    def get_note(self):
        cursor = get_cursor()
        cursor.execute("SELECT * FROM StudentNote WHERE assigment_code = ? AND assigment_name = ?", (self.assigment_code, self.assigment_name))
        result = cursor.fetchone()
        cursor.close()

        if result: return result

        return None


    @staticmethod
    def get_note(assigment_code, assigment_name):
        cursor = get_cursor()
        cursor.execute("SELECT * FROM StudentNote WHERE assigment_code = ? AND assigment_name = ?", (assigment_code, assigment_name))
        result = cursor.fetchone()
        cursor.close()

        if result: return result

        return None


    @staticmethod
    def create_note(assigment_code, assigment_name, note, court):
        cursor = get_cursor()

        cursor.execute(f"INSERT INTO StudentNote (id, court_{court}, assigment_code, assigment_name) VALUES (?, ?, ?, ?)", (str(uuid.uuid4()), note, assigment_code, assigment_name))

        commit_db()

        cursor.close()

        return StudentNote.get_note(assigment_code, assigment_name)


    @staticmethod
    def update_note(assigment_code, assigment_name, note, court):
        cursor = get_cursor()

        cursor.execute(f"UPDATE StudentNote SET court_{court} = ? WHERE assigment_code = ? AND assigment_name = ?", (note, assigment_code, assigment_name))
        commit_db()
        cursor.close()


        return StudentNote.get_note(assigment_code, assigment_name)
