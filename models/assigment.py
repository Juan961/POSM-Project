import uuid

from data import ASSIGNEMETS

class Assigment:
    def __init__(self, name, teacher_id) -> None:
        self.id = str(uuid.uuid4())

        self.name = name
        self.teacher = teacher_id
        self.students = []

        ASSIGNEMETS.append(self)

    def __str__(self):
        return self.name

    @staticmethod
    def get_assigment(id):
        for assigment in ASSIGNEMETS:
            if assigment.id == id:
                return assigment 

        return None

    @staticmethod
    def get_all_assigments(id):
        return ASSIGNEMETS
