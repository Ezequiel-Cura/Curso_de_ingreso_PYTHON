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
Al presionar el botón ‘Validar letra’, mediante prompt solicitar al usuario que ingrese una letra. 
Se deberá validar que la letra sea ‘U’, ‘T’ o ‘N’ (en mayusculas) 
En caso no coincidir con ninguna de las letras, volverla a solicitar hasta que la condición se cumpla
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_validar_letra = customtkinter.CTkButton(master=self, text="Ingresar", command=self.btn_validar_letra_on_click)
        self.btn_validar_letra.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_validar_letra_on_click(self):
        letra_ingresada = prompt(title="Letras",prompt="Ingrese una letra")
        if len(letra_ingresada) > 1:
            letra_ingresada = prompt(title="Letras",prompt="Solo una letra")            
        flag = True
        # while letra not in ["U","T","N"]:
        while flag:
            if letra_ingresada == "U" or letra_ingresada == "T" or letra_ingresada == "N": 
                flag = False
            else:
                letra_ingresada = prompt(title="Letras",prompt="Reintentar")
            
            # match letra_ingresada:
            #     case "U" | "T" | "N":
            #         flag = False
            #     case _:
            #         letra_ingresada = prompt(title="Letras",prompt="Reintentar")
                    
        alert("Ej 05", "Muy bien!")
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()