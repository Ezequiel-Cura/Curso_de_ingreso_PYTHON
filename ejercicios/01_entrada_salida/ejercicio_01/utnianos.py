import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Pablo Francisco
apellido: López
---
Ejercicio: entrada_salida_01
---
Enunciado:
Al presionar el  botón, se debe mostrar un mensaje como el siguiente "Esto no anda, funciona".
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        
        contador_femenino = 0
        acumulador_edad_femenina = 0

        contador_masculino = 0


        for a in range(100):
        
            #ingreso de nombre
            nombre = prompt("Votación", "Ingrese su nombre")
            for index in range(0, 100, 1):
                        # inicio  fin   pasos
                if nombre != "" and nombre != None:
                    break
                nombre = prompt("ERROR", "Reingrese su nombre")
            

            #ingreso de edad
            #edad = prompt("Votación", "Ingrese su edad. Debe ser mayor de 13 años")
            for index in range(0, 100, 1):
                edad = prompt("Votación", "Ingrese su edad. Debe ser mayor de 13 años")
                edad = int(edad)
                if edad > 13:                 
                    break

            
            #ingreso de genero
            for index in range(0, 100, 1):
                genero = prompt("Votacion", "Ingrese su género (masculino, femenino u otro)")
                if genero == "masculino" or genero == "femenino" or genero == "otro":
                    break
                


            #ingreso de votación
            for index in range(0, 100, 1):
                nominado = prompt("Votación", "Ingrese a quién va a votar (Giovanni, Gianni o Facundo)")
                if nominado == "Giovanni" or nominado == "Gianni" or nominado == "Facundo":
                    break

            #match separacion por genero
            match genero:
                case "femenino":
                    contador_femenino = contador_femenino + 1
                    acumulador_edad_femenina = acumulador_edad_femenina + edad
                case "masculino":
                    if edad > 24 and edad < 41:
                        break
                case _:
                    pass

            respuesta = question("Nominados", "Desea continuar?")
            if respuesta == False:
                break
        
        if contador_femenino == 0:
            promedio_edad_femenino = 0
        else:
            promedio_edad_femenino = acumulador_edad_femenina / contador_femenino
        
        alert("Uteniano", promedio_edad_femenino)





if __name__ == "__main__":
    app = App()
    app.mainloop()