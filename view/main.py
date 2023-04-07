import tkinter as tk
from tkinter import ttk

from .student import StudentView 
from .professor import ProfessorView 

class MainView:
    def __init__(self) -> None:
        self.main_window = tk.Tk()
        self.main_window.title("Project")
        self.main_window.geometry("800x600")

        ttk.Button(self.main_window, text="Soy estudiante", command=StudentView).grid(row=0, column=0)
        ttk.Button(self.main_window, text="Soy docente", command=ProfessorView).grid(row=0, column=1)
        ttk.Button(self.main_window, text="Salir", command=self.main_window.destroy).grid(row=1, column=0, columnspan=2)

        self.main_window.mainloop()
