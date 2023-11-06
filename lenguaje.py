import re
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageTk

grammar_rules = [
    (r"^\s*(A1|A2|A3)\s+[a-zA-Z_][a-zA-Z_]*\s*$", "Declaración de variable"),
    (r"^\s*(C1)\s*\(\s*([a-zA-Z_][a-zA-Z_]*)\s*([<>=!]=?)\s*([a-zA-Z_][a-zA-Z_]*|\d+)\s*\)\s*:\s*(.*)\s*;\s*$", "Declaración de condicional"),
    (r"^\s*(init)\s+([a-zA-Z_][a-zA-Z_]*)\s*\(([a-zA-Z_][a-zA-Z_]*)\)\s*:\s*(.*)\s*;\s*$", "Declaración de función"),
    (r"^\s*F1\s*\(\s*([a-zA-Z_][a-zA-Z_]*[<>!=]+[^,]+)\s*\):\s*(.*?)\s*;\s*$", "Declaración de ciclo con una condicional"),
    (r"^\s*F1\s*\(\s*([a-zA-Z_][a-zA-Z_]*[<>!=]+[^,]+,\s*[a-zA-Z_][a-zAZ_]*[<>!=]+[^,]+)\s*\):\s*(.*?)\s*;\s*$", "Declaración de ciclo con dos condicionales"),
    (r"^\s*F1\s*\(\s*([a-zA-Z_][a-zA-Z_]*[<>!=]+[^,]+,\s*[a-zA-Z_][a-zA-Z_]*[<>!=]+[^,]+,\s*[a-zA-Z_][a-zA-Z_]*[<>!=]+[^,]+)\s*\):\s*(.*?)\s*;\s*$", "Declaración de ciclo con tres condicionales")

]

class inicio(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ventana Principal")
        self.geometry("600x400")
        self.configure(bg="#333")
        self._frame = None
        self.crear_interfaz()

    def crear_interfaz(self):
        self.label = tk.Label(self, text="Pika", font=('Arial', 16),bg="#333",fg="white")
        self.label.place(x=266, y=30)
        self.label = tk.Label(self, text="Py", font=('Arial', 16),bg="#333",fg="yellow")
        self.label.place(x=308, y=30)
        self.label = tk.Label(self, text="Ingrese una declaración (variable, condicional, función o ciclo)", font=('Arial', 12),bg="#333",fg="white")
        self.label.place(x=70, y=120)

        self.entry_variable = tk.Entry(self, font=('Arial', 16), width=40, relief="solid", borderwidth=2)
        self.entry_variable.place(x=50, y=150)

        estilo_boton = {
            'font': ('Arial', 20, 'bold'), 
            'fg': '#333',
            'bg': 'white',
            'width': 11,
            'height': 0,
            'relief': 'raised',
            'borderwidth': 2,
        }

        self.button_login = tk.Button(self, text="Iniciar",command=self.validar, **estilo_boton)
        self.button_login.place(x=200, y=220)


        self.resultado_label = tk.Label(self, text="",font=('Arial', 12),bg="#333",fg="white")
        self.resultado_label.place(x=200, y=330)

    def validar_declaracion(self):
        for self.pattern, self.regla in grammar_rules:
            if re.match(self.pattern, self.declaracion):
                return self.regla + " válida."
        return "Error en la declaración."

    def validar(self):
        self.declaracion = self.entry_variable.get()
        resultado = self.validar_declaracion()
        self.resultado_label.config(text=resultado)

       
if __name__ == "__main__":
    app = inicio()
    app.mainloop()