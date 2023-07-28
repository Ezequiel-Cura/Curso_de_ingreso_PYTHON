import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Ezequiel
Apellido: Cura
Entregado
Al presionar el botón Mostrar pedir un número. mostrar los números divisores desde el 1 al número ingresado, 
y mostrar la cantidad de números divisores encontrados.
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
        numero_ingresado = prompt("Ej 07","Ingrese un numero")
        if numero_ingresado != None and numero_ingresado.isdigit():
            numero_ingresado = int(numero_ingresado)    
            for i in range(1,numero_ingresado + 1,1):                        
                if numero_ingresado % i == 0:
                    print(f"Numero divisor: {i}")
                    contador +=1

        print(f"Se encontrar un total de {contador} divisores de {numero_ingresado}")
        
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()