import tkinter as tk
from tkinter import ttk

# Alfabeto aceptado
alfabeto = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-")



# Tabla de transiciones
tablaTrancision = [[0,'F',1], [1,'R',2], [1,'S',2], [1,'T',2], [1,'U',2], [1,'V',2], [1,'W',2],
          [2,'A',3], [2,'B',3], [2,'C',3], [2,'D',3], [2,'E',3], [2,'F',3], [2,'G',3], 
          [2,'H',3], [2,'I',3], [2,'J',3], [2,'K',3], [2,'L',3], [2,'M',3], [2,'N',3], 
          [2,'O',3], [2,'P',3], [2,'Q',3], [2,'R',3], [2,'S',3], [2,'T',3], [2,'U',3], 
          [2,'V',3], [2,'W',3], [2,'X',3], [2,'Y',3], [2,'Z',3], [3,'-',4], [4,'1',5], 
          [4,'2',5], [3,'3',4], [3,'4',4], [3,'5',4], [3,'6',4], [4,'7',5], [4,'8',5], 
          [4,'9',5], [5,'1',6], [5,'2',6], [5,'3',6], [5,'4',6], [5,'5',6], [5,'6',6], 
          [5,'7',6], [5,'8',6], [5,'9',6], [6,'1',7], [6,'2',7], [6,'3',7], [6,'4',7], 
          [6,'5',7], [6,'6',7], [6,'7',7], [6,'8',7], [6,'9',7], [5,'0',8], [8,'0',9], 
          [8,'1',9], [8,'2',9], [8,'3',9], [8,'4',9], [8,'5',9], [8,'6',9], [8,'7',9], 
          [8,'8',9], [8,'9',9], [6,'0',9], [4,'0',10], [10,'0',11], [11,'1',13], [11,'2',13], [11,'3',13], [11,'4',13], 
          [11,'5',13], [11,'6',13], [11,'7',13], [11,'8',13], [11,'9',13], [10,'1',12], [10,'2',12], [10,'3',12], [10,'4',12], 
          [10,'5',12], [10,'6',12], [10,'7',12], [10,'8',12], [10,'9',12], [12,'0',13], [12,'1',13], [12,'2',13], [12,'3',13], [12,'4',13], 
          [12,'5',13], [12,'6',13], [12,'7',13], [12,'8',13], [12,'9',13], [7,'-',14], [9,'-',14], [13,'-',14],
          [14,'A',15], [14,'B',15], [14,'C',15], [14,'D',15], [14,'E',15], [14,'F',15], [14,'G',15], 
          [14,'H',15], [14,'I',15], [14,'J',15], [14,'K',15], [14,'L',15], [14,'M',15], [14,'N',15], 
          [14,'O',15], [14,'P',15], [14,'Q',15], [14,'R',15], [14,'S',15], [14,'T',15], [14,'U',15], 
          [14,'V',15], [14,'W',15], [14,'X',15], [14,'Y',15], [14,'Z',15] ]


#obtener trancisiones en base a al estado actual y el caracter actual
def obtener_transicion(estado_actual, caracter_actual):
    for fila in tablaTrancision:
        if estado_actual == fila[0] and caracter_actual == fila[1]:
            return fila[2]
    return None


# Estado Final 
EF = [15]

# Estado Inicial 
EI = 0

# Función para validar la cadena de entrada
def validar_cadena():
    global CE, ea, tablaComparacion, bandera
    
    CE = entrada.get()
    
    # Tabla de estado de la comparación
    tablaComparacion = []

    # Bandera por si la entrada no pertenece al alfabeto de entrada
    bandera = True

    # Estado Actual 
    ea = EI 
    
    for caracter in CE: # Iterar a través de cada caracter en la cadena de entrada
        if caracter in alfabeto:
            nueva_transicion = obtener_transicion(ea, caracter)
            if nueva_transicion is not None:  # Verificar si se encontró una transición válida
                tablaComparacion.append([ea, caracter, nueva_transicion])
                ea = nueva_transicion
            else:
                bandera = False
                break
        else:
            bandera = False

    if ea in EF and bandera:
        resultado.config(text="CADENA VALIDA", fg="green")
    else:
        resultado.config(text="CADENA NO VALIDA", fg="red")
        
    # Actualizar el widget Text con la tabla de comparación
    mostrar_tabla_comparacion(tablaComparacion)

# Función para mostrar la tabla de comparación en el widget Text
def mostrar_tabla_comparacion(tabla):
    tabla_text.delete(1.0, "end")  # Borra el contenido anterior
    for fila in tabla:
        tabla_text.insert("end", f"Estado Actual: {fila[0]}, Caracter: {fila[1]}, Nuevo Estado: {fila[2]}\n")


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Validador de matriculas")
ventana.geometry("300x250") 

# Campo de entrada
etiqueta = tk.Label(ventana, text="Ingrese la matricula:")
etiqueta.pack()
entrada = tk.Entry(ventana, font=("Arial", 16))
entrada.pack()

# Botón para validar
boton = tk.Button(ventana, text="Validar", command=validar_cadena, font=("Arial", 16))
boton.pack()

# Mostrar el resultado
resultado = tk.Label(ventana, text="", fg="black", font=("Arial", 16))
resultado.pack()

# Mostrar la tabla de comparación
tabla_text = tk.Text(ventana, height=10, width=40, font=("Arial", 14))
tabla_text.pack()

# Iniciar la interfaz gráfica
ventana.mainloop()