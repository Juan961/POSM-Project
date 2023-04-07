from models import Student, Professor, Assigment

from view import Main

def main():
    try:
        main_es = Student("Juan")
        main_pr = Professor("Juan")
        main_as = Assigment("juan", main_pr.id)

        Main()

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
