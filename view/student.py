import tkinter as tk
from tkinter import ttk

from models import Student, Professor, Assigment

class StudentView:
    def __init__(self) -> None:
        root = tk.Tk()
        root.title("Notas")

        frame = ttk.Frame(root, padding="3")
        frame.pack(fill="both", expand=True)

        self.table = ttk.Treeview(frame, columns=("nombre", "Cor_1","Cor_2","Notaf"))

        # Definir encabezados de columna
        self.table.heading("#0", text="ID")
        self.table.heading("nombre", text="Materia")
        self.table.heading("Cor_1", text="Corte 1")
        self.table.heading("Cor_2", text="Corte 2")
        self.table.heading("Notaf", text="Nota final")
        self.table.pack(side="left", fill="both", expand=True)

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

        # Crear botón para agregar datos a la tabla
        self.boton_volver = ttk.Button(frame, text="Volver a escojer rol", command=root.destroy)
        self.boton_volver.pack(pady=10)
        self.boton_salir = ttk.Button(root, text="Salir", command=root.destroy)
        self.boton_salir.pack(pady=10)
        self.boton_agregar = ttk.Button(root, text="Agregar", command=self.insertar_datos)

        # Agregar widgets al Frame principal
        ttk.Label(root, text="Nombre").pack(side="top", padx=0, pady=0) 
        self.materia_entry.pack(side="top", padx=0, pady=0)

        ttk.Label(root, text="Laboratorio 1er corte:").pack(side="top", padx=10, pady=5)
        self.labo1_entry.pack(side="top", padx=10, pady=5)
        ttk.Label(root, text="Proyecto 1er corte:").pack(side="top", padx=10, pady=5)
        self.Pory1_entry.pack(side="top", padx=10, pady=5)
        ttk.Label(root, text="Parcial 1er corte: ").pack(side="top", padx=10,pady=5)
        self.Par1_entry.pack(side="top", padx=10, pady=5)
        
        ttk.Label(root, text="Laboratorio 2do corte:").pack(side="top", padx=10, pady=5)
        self.labo2_entry.pack(side="top", padx=10, pady=5)
        ttk.Label(root, text="Proyecto 2do corte:").pack(side="top", padx=10, pady=5)
        self.Pory2_entry.pack(side="top", padx=10, pady=5)
        ttk.Label(root, text="Parcial 2do corte: ").pack(side="top", padx=10,pady=5)
        self.Par2_entry.pack(side="top", padx=10, pady=5)

        ttk.Label(root, text="Laboratorio 3er corte:").pack(side="top", padx=10, pady=5)
        self.labo3_entry.pack(side="top", padx=10, pady=5)
        ttk.Label(root, text="Proyecto 3er corte:").pack(side="top", padx=10, pady=5)
        self.Pory3_entry.pack(side="top", padx=10, pady=5)
        ttk.Label(root, text="Parcial 3er corte: ").pack(side="top", padx=10,pady=5)
        self.Par3_entry.pack(side="top", padx=10, pady=5)

        self.boton_agregar.pack(side="top", padx=10, pady=10)

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
        self.materia_entry .delete(0, tk.END)

        self.labo1_entry.delete(0, tk.END)
        self.Pory1_entry.delete(0, tk.END)
        self.Par1_entry.delete(0,tk.END)

        self.labo2_entry.delete(0, tk.END)
        self.Pory2_entry.delete(0, tk.END)
        self.Par2_entry.delete(0,tk.END)

        self.labo3_entry.delete(0, tk.END)
        self.Pory3_entry.delete(0, tk.END)
        self.Par3_entry.delete(0,tk.END)
