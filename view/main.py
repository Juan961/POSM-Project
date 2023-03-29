import tkinter as tk

from models import Student, Professor, Assigment

class StudentsTable:

    def __init__(self, root, rows, columns, matrix):

        self.e = tk.Entry(root, width=20)

        for i in range(rows):
            for j in range(columns):

                self.e.grid(row=i, column=j)
                self.e.insert(j, "asd")

        self.e.place(x=80, y=100)

main_window = tk.Tk()

main_window.geometry('500x500')

main_window.title("Project")

tk.Label(main_window, text="Students: ").place(x=80, y=50)

table = StudentsTable(main_window, len(Student.get_all_students()), 2, Student.get_all_students())
