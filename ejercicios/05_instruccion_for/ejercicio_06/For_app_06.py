import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Ezequiel
Apellido: Cura
Entregado
Al presionar el botón Mostrar pedir un número. mostrar los números pares desde 
el 1 al número ingresado, y mostrar la cantidad de números pares encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        contador = 0
        numero_ingresado = prompt("Ej 06","Ingrese un numero")
        if numero_ingresado != None and numero_ingresado.isdigit():
            numero_ingresado = int(numero_ingresado)
            for i in range(0,numero_ingresado,2):
                print(f"Numero par:{i}")
                contador += 1
        
        print(f"Se encontraron un total de {contador} numeros pares")
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()