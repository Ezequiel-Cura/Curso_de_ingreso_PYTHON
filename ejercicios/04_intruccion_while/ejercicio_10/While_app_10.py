import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Ezequiel
Apellido: Cura
Entregado
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        cantidad_positivos = 0
        cantidad_negativos = 0
        cantidad_ceros = 0
        
        suma_positivos = 0
        suma_negativos = 0
        contador = 0
        while True:
            numero = prompt("Numero",f"Ingrese un numero({contador})")     
            if numero == None:
                break
            # if numero.isdigit():    
            numero = int(numero)
            
            if numero < 0:
                cantidad_negativos += 1
                suma_negativos += numero
            elif numero > 0:
                cantidad_positivos += 1
                suma_positivos += numero
            else:
                cantidad_ceros += 1
            contador +=1
                
        alert("ej 10",f"Suma de positivos: {suma_positivos} \nSuma de negativos: {suma_negativos} \nCantidad de positivos: {cantidad_positivos} \nCantidad de negativos: {cantidad_negativos} \nCantidad de ceros: {cantidad_ceros} \nLa diferencia entre la cantidad de positivos y negativos es: {cantidad_positivos - cantidad_negativos}")
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
