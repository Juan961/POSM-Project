import uuid

from data import STUDENTS, PROFESSORS, ASSIGNEMETS

from .assigment import Assigment

class Professor:
    def __init__(self, name) -> None:
        self.id = str(uuid.uuid4())

        self.name = name
        self.assigments = []

        PROFESSORS.append(self)

    def __str__(self):
        return self.name

    @staticmethod
    def get_teacher(id):
        for professor in PROFESSORS:
            if professor.id == id:
                return professor 

        return None

    @staticmethod
    def create_assigment(teacher_id, assigment_name):
        professor = Professor.get_teacher(teacher_id)
        if not professor: raise Exception("Professor not found")

        assigment = Assigment(assigment_name, professor.id)

        return assigment
