import uuid

from data import ASSIGNEMETS

class Note:
    def __init__(self, user_id, assigment_id, court, value_percentage) -> None:
        self.id = str(uuid.uuid4())

        self.user = user_id
        self.assigment = assigment_id
        self.court = court
        self.value_percentage = value_percentage

    @staticmethod
    def get_assigment(id):
        for assigment in ASSIGNEMETS:
            if assigment.id == id:
                return assigment 

        return None

    @staticmethod
    def get_all_assigments(id):
        return ASSIGNEMETS
