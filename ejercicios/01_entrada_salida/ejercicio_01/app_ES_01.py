import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Ezequiel
apellido: Cura
Entregado
---
Ejercicio: entrada_salida_01
---
Enunciado:
Al presionar el  botón, se debe mostrar un mensaje como el siguiente "Esto no anda, funciona".

        contador_fuego = 0
        contador_electrico = 0
        
        nombre_poder_alto = None
        tipo_poder_alto = None
        poder_poder_alto = None

        nombre_poder_bajo = None
        tipo_poder_bajo = None
        poder_poder_bajo = None
        
        contador_poke_mas_100 = 0
        contador_poke_menos_100 = 0
        
        tipo_pokemons_mas_posea = None
        tipo_pokemons_menos_posea = None
        
        promedio_poder = None
        promedio_poder_electrico = None
        
        for tipo in self.lista_tipo:
            match tipo:
                case "fuego":
                    contador_fuego += 1
                case "electrico":
                    contador_electrico +=1
        
        flag_poder = True
        for poder in self.lista_poder:
            if flag_poder == True:
                nombre_poder_alto = self.lista_nombre[0]
                nombre_poder_bajo = self.lista_nombre[0]
       
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        """Agregue una linea"""
        alert(title="EJ 01",message="Esto no anda, funciona")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
