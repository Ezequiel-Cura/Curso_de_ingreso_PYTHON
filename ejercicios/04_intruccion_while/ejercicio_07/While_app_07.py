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
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario quiera, 
hasta que presione el botón Cancelar (en el prompt). 
Calcular la suma acumulada y el promedio de los números ingresados. 
Luego informar los resultados en las cajas de texto txt_suma_acumulada y txt_promedio

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
        
        self.txt_suma_acumulada = customtkinter.CTkEntry(master=self, placeholder_text="Suma acumulada")
        self.txt_suma_acumulada.grid(row=0, padx=20, pady=20)

        self.txt_promedio = customtkinter.CTkEntry(master=self, placeholder_text="Promedio")
        self.txt_promedio.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        suma = 0
        vueltas = 0
        numero = 0
        while numero != None:
            numero = prompt("Numero",f"Ingrese un numero({vueltas})")
            if numero != None and numero.isdigit(): # Si no esta vacio y es un numero lo transformamos en int
                numero_int = int(numero)
            else: # Si no es un numero salteamos lo que queda de esta vuelta y pedimos el prompt denuevo
                continue
            suma += numero_int # Si entra al else, se saltea estas dos lineas y empieza la proxima vuelta
            vueltas +=1

        if vueltas == 0:
            promedio = 0
        else:
            promedio = suma / vueltas
        
        self.txt_suma_acumulada.delete(0,100)
        self.txt_promedio.delete(0,100)
        
        self.txt_suma_acumulada.insert(0,suma)
        self.txt_promedio.insert(0,promedio)
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
