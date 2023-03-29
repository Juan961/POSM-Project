from models import Student, Professor, Assigment

from view.main import main_window

def main():
    try:
        es_1 = Student("Juan")
        pro_1 = Professor("Juan")
        as_1 = Assigment("juan", pro_1.id)

        # main_window.mainloop()

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
