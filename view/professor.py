import tkinter as tk
from tkinter import ttk

from models import Student, Professor, Assigment

class ProfessorView:
    def __init__(self) -> None:
        root = tk.Tk()
        root.title("Notas")

        frame = ttk.Frame(root, padding="20")
        frame.grid(row=1, column=0, columnspan=5)

        self.table = ttk.Treeview(frame, columns=("nombre", "Cor_1", "Cor_2", "Cor_3", "Notaf"))

        # Definir encabezados de columna
        self.table.heading("#0", text="ID")
        self.table.heading("nombre", text="Estudiante")
        self.table.heading("Cor_1", text="Corte 1")
        self.table.heading("Cor_2", text="Corte 2")
        self.table.heading("Cor_3", text="Corte 3")
        self.table.heading("Notaf", text="Nota final")
        self.table.grid(row=1, column=0, columnspan=5)

        # Crear widgets para ingresar datos
        self.materia_entry = ttk.Entry(root, width=20)

        self.labo1_entry = ttk.Entry(root, width=5)
        self.Pory1_entry = ttk.Entry(root, width=5)
        self.Par1_entry = ttk.Entry(root, width=5)

        self.labo2_entry = ttk.Entry(root, width=5)
        self.Pory2_entry = ttk.Entry(root, width=5)
        self.Par2_entry = ttk.Entry(root, width=5)

        self.labo3_entry = ttk.Entry(root, width=5)
        self.Pory3_entry = ttk.Entry(root, width=5)
        self.Par3_entry = ttk.Entry(root, width=5)

        self.boton_volver = ttk.Button(frame, text="Volver a escojer rol", command=root.destroy).grid(row=0, column=4, pady=10)
        self.boton_agregar = ttk.Button(root, text="Agregar", command=self.insertar_datos)

        # Agregar widgets al Frame principal
        ttk.Label(root, text="Nombre").grid(row=2, column=1)
        self.materia_entry.grid(row=2, column=2)

        ttk.Label(root, text="Primer corte").grid(row=4, column=0, pady=10)

        ttk.Label(root, text="Laboratorio").grid(row=5, column=0)
        self.labo1_entry.grid(row=6, column=0)
        ttk.Label(root, text="Proyecto").grid(row=7, column=0)
        self.Pory1_entry.grid(row=8, column=0)
        ttk.Label(root, text="Parcial").grid(row=9, column=0)
        self.Par1_entry.grid(row=10, column=0)

        ttk.Label(root, text="Segundo corte").grid(row=4, column=2, pady=10)

        ttk.Label(root, text="Laboratorio").grid(row=5, column=2)
        self.labo2_entry.grid(row=6, column=2)
        ttk.Label(root, text="Proyecto").grid(row=7, column=2)
        self.Pory2_entry.grid(row=8, column=2)
        ttk.Label(root, text="Parcial").grid(row=9, column=2)
        self.Par2_entry.grid(row=10, column=2)

        ttk.Label(root, text="Tercer corte").grid(row=4, column=4, pady=10)

        ttk.Label(root, text="Laboratorio").grid(row=5, column=4)
        self.labo3_entry.grid(row=6, column=4)
        ttk.Label(root, text="Proyecto").grid(row=7, column=4)
        self.Pory3_entry.grid(row=8, column=4)
        ttk.Label(root, text="Parcial").grid(row=9, column=4)
        self.Par3_entry.grid(row=10, column=4)

        self.boton_agregar.grid(row=12, column=2, pady=10)

        root.mainloop()

    def insertar_datos(self):
        # Obtener valores ingresados por el usuario
        nombre = self.materia_entry.get()

        nlab1 = float(self.labo1_entry.get())
        npro1 = float(self.Pory1_entry.get())
        npar1 = float(self.Par1_entry.get())
        cor1n= (nlab1*(1/3))+(npro1*(1/3))+(npar1*(1/3))

        nlab2 = float(self.labo2_entry.get())
        npro2 = float(self.Pory2_entry.get())
        npar2 = float(self.Par2_entry.get())
        cor2n= (nlab2*(1/3))+(npro2*(1/3))+(npar2*(1/3))

        nlab3 = float(self.labo3_entry.get())
        npro3 = float(self.Pory3_entry.get())
        npar3 = float(self.Par3_entry.get())
        cor3n= (nlab3*(3/10))+(npro3*(3/10))+(npar3*(4/10))

        notaf=(cor1n*0.3)+(cor2n*0.3)+(cor3n*0.4)

        # Insertar datos en la tabla
        id = len(self.table.get_children()) + 1
        self.table.insert("", "end", text=id, values=(nombre, cor1n, cor2n, cor3n, notaf))

        # Limpiar widgets de entrada
        self.materia_entry.delete(0, tk.END)

        self.labo1_entry.delete(0, tk.END)
        self.Pory1_entry.delete(0, tk.END)
        self.Par1_entry.delete(0,tk.END)

        self.labo2_entry.delete(0, tk.END)
        self.Pory2_entry.delete(0, tk.END)
        self.Par2_entry.delete(0,tk.END)

        self.labo3_entry.delete(0, tk.END)
        self.Pory3_entry.delete(0, tk.END)
        self.Par3_entry.delete(0,tk.END)
