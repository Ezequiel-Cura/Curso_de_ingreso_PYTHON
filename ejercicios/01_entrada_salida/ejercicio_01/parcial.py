import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Ezequiel
Apellido: Cura
DNI: 44160534

A) El profesor OAK de pueblo paleta quiere que construyas un modelo prototipico de pokedex con 
 algunos pokemones de prueba.

Para ello deberas programar el boton "Cargar Pokedex" para poder cargar 10 pokemones.
Los datos que deberas pedir para los pokemones son:
    * El nombre del pokemon
    * El tipo de su elemento (Agua, Tierra, Psiquico, Fuego, Electrico)
    * La cantidad de poder (validar que sea mayor a 50 y menor a 200)
    
-- SOLO SE CARGARAN LOS VALORES SI Y SOLO SI SON CORRECTOS --

#B) Al presionar el boton mostrar, se debera mostrar el pokemon (nombre, tipo y poder) de tipo fuego o agua con mas poder

Para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    1- Tome el ultimo numero de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)

    2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). 
    Realiza el informe correspondiente al numero obtenido.
    
EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 

*******Tener en cuenta que pueden no haber ingresos o egresos**********
C) Al presionar el boton Informar 
    # 0) - Cantidad de pokemones de tipo Fuego
    # 1) - Cantidad de pokemones de tipo Electrico
    # 2) - Nombre, tipo y Poder del pokemon con el poder mas alto
    # 3) - Nombre, tipo y Poder del pokemon con el poder mas bajo
    # 4) - Cantidad de pokemones, con mas de 100 de poder.
    # 5) - Cantidad de pokemones, con menos de 100 de poder
    # 6) - tipo de los pokemones del tipo que mas pokemones posea 
    # 7) - tipo de los pokemones del tipo que menos pokemones posea 
    # 8) - el promedio de poder de todos los ingresados
    # 9) - el promedio de poder de todos los poquemones de Electrico 

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("Simulacro Parcial")

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Pokedex", command=self.btn_cargar_on_click)
        self.btn_cargar.grid(row=3, padx=20, pady=20, columnspan=2, sticky="nsew")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.btn_informar= customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=5, padx=20, pady=20, columnspan=2, sticky="nsew")        

        # self.lista_nombre = ["eze","quien","pikachu","formosa","santiago","pepe"]
        # self.lista_tipo = ["fuego","agua","electrico","tierra","agua","fuego"]
        # self.lista_poder = [100,150,200,59,120,195]

        self.lista_nombre = []
        self.lista_tipo = []
        self.lista_poder = []
        
    def btn_cargar_on_click(self):
        
        for i in range(10):
            
            while True:
                nombre = prompt("UTN",f"Ingrese nombre ({i})")
                if nombre != None and nombre != "":
                    self.lista_nombre.append(nombre)
                    break
            
            while True:
                tipo = prompt("UTN","Ingrese tipo\n(Agua, Tierra, Psiquico, Fuego, Electrico)")
                if tipo != None and tipo != "":
                    tipo = tipo.lower()
                    if tipo == "agua" or tipo == "tierra" or tipo == "psiquico" or tipo == "fuego" or tipo == "electrico":
                        self.lista_tipo.append(tipo)
                        break
                
            while True:
                poder = prompt("UTN","Ingrese poder")
                if poder != None and poder != "":
                    poder = int(poder)
                    if poder >= 50 and poder <= 200:
                        self.lista_poder.append(poder)
                        break
            
            respuesta = question("UTN","desea continuar?")
            if not respuesta:
                break
    
    def btn_mostrar_on_click(self):
        #B) Al presionar el boton mostrar, se debera mostrar el pokemon (nombre, tipo y poder) de tipo fuego o agua con mas poder
        nombre_pokemon = None
        tipo_pokemon = None
        poder_pokemon = None
        
        flag_primero = True
        if len(self.lista_poder) > 0:
            
            for i in range(len(self.lista_poder)):
                
                if flag_primero == True and (self.lista_tipo[i] == "fuego" or self.lista_tipo[i] == "agua"):
                    nombre_pokemon = self.lista_nombre[i]
                    tipo_pokemon = self.lista_tipo[i]
                    poder_pokemon = self.lista_poder[i]
                    flag_primero = False
                elif (self.lista_tipo[i] == "fuego" or self.lista_tipo[i] == "agua") and poder_pokemon < self.lista_poder[i]:
                    nombre_pokemon = self.lista_nombre[i]
                    tipo_pokemon = self.lista_tipo[i]
                    poder_pokemon = self.lista_poder[i]          
        
        alert("UTN",f"Nombre: {nombre_pokemon}\nTipo: {tipo_pokemon}\nPoder:{poder_pokemon}") 
               
    def btn_informar_on_click(self):
        # 4) - Cantidad de pokemones, con mas de 100 de poder.
        # 5) - Cantidad de pokemones, con menos de 100 de poder
        cantidad_pokemons_mas_100 = 0
        cantidad_pokemons_menos_100 = 0
        
        for poder in self.lista_poder:
            if poder > 100:
                cantidad_pokemons_mas_100 += 1
            if poder <= 100:
                cantidad_pokemons_menos_100 += 1

        alert("UTN",f"Cantidad de pokemons con mas de 100 de poder: {cantidad_pokemons_mas_100}\nCantidad de pokemons con menos de 100 de poder: {cantidad_pokemons_menos_100}")
        
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()