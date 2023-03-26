from data import STUDENTS, PROFESSORS, ASSIGNEMETS

from models import Student, Professor, Assigment

def main():
    try:
        es_1 = Student("Juan")

        pro_1 = Professor("Juan")

        as_1 = Assigment("juan", pro_1.id)

        print(Student.get_student(es_1.id))
    
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
