import tkinter as tk
from tkinter import ttk

from .student import StudentView 
from .professor import ProfessorView 

class MainView:
    def __init__(self) -> None:
        main_window = tk.Tk()
        main_window.title("Project")

        boton_tabla1 = ttk.Button(main_window, text="Soy estudiante", command=StudentView)
        boton_tabla1.pack(padx=10, pady=10)
        boton_tabla2 = ttk.Button(main_window, text="Soy docente", command=ProfessorView)
        boton_tabla2.pack(padx=10, pady=10)
        boton_salir = ttk.Button(main_window, text="Salir", command=main_window.destroy)
        boton_salir.pack(pady=10)

        main_window.mainloop()
