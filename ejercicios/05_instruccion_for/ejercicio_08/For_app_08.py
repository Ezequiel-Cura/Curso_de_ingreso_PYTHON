import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Ezequiel
Apellido: Cura
Entregado
Al presionar el botón Mostrar pedir un número. Informar si el número es PRIMO o no.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        mensaje = None
        numero_ingresado = prompt("Ej 08","Ingrese un numero")
        if numero_ingresado != None and numero_ingresado.isdigit():
            numero_ingresado = int(numero_ingresado)
            for n in range(2, numero_ingresado ):
                if numero_ingresado % n == 0: #Si encuentra algun numero que es divisor corta ya que no es primo
                    mensaje = "No es primo"
                    break 
            if mensaje == None:           
                mensaje = "Es primo"
            print(mensaje)
            
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()