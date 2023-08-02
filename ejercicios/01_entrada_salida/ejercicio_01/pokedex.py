# Copyright (C) 2023 <UTN FRA>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
#El profesor OAK de pueblo paleta quiere que construyas un modelo prototipico de pokedex con algunos pokemones de prueba.

A) Para ello deberas programar el boton "Cargar Pokedex" para poder cargar 10 pokemones.
Los datos que deberas pedir para los pokemones son:
    * El nombre del pokemon
    * El tipo de su elemento (Agua, Psiquico, Fuego)
    * Poder de ataque (validar que sea mayor a 50 y menor a 200)
B) Al presionar el boton mostrar se deberan listar los pokemones y su posicion en la lista (por terminal) 

Del punto C solo debera realizar 3 informes. Para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    Informe 1- Tome el ultimo numero de su DNI Personal (Ej 4) y realice ese informe (Ej, Realizar informe 4)
    3
    
    Informe 2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). En caso de que su DNI 
    finalice con el numero 0, debera realizar el informe 9.
    6
    
    
    Informe 3- Tome la suma de los ultimos dos numeros de su DNI personal, en caso de ser un numero par, tomara el numero par 
    mas chico que su ultimo digito del DNI (en caso de que su ultimo digito sea 2, resolvera el ejercicio 8). En caso contrario
    , si es impar, tomara el numero impar posterior (en caso de que su ultimo digito sea 9, resolvera el ejercicio 1)
    En caso de que el numero sea el mismo obtenido en el informe 2, realizara el siguiente informe en la lista.
    
    
    Realizar los informes correspondientes a los numeros obtenidos. EL RESTO DE LOS INFORMES LOS DEBE IGNORAR. 
C) 
    #! 0) - Cantidad de pokemones de tipo Fuego cuyo poder de pelea con un 10% extra supere los 100 puntos.
    #! 1) - Cantidad de pokemones de tipo Psiquico cuyo poder de pelea con un 15% menos este entre los 100 y los 150 puntos.
    #! 2) - Nombre y Poder del pokemon de tipo Agua con el poder mas alto.
    #! 3) - Nombre y Poder del pokemon de tipo Psiquico con el poder mas bajo.
    #! 4) - Porcentaje de pokemones de tipo agua con mas de 100 puntos de poder (Sobre el total de pokemones ingresados).
    #! 5) - Porcentaje de pokemones de tipo psiquico con poder de pelea inferior o igual a 150 (sobre el total de pokemones ingresados).
    #! 6) - tipo de los pokemones del tipo que mas pokemones posea. 
    #! 7) - tipo de los pokemones del tipo que menos pokemones posea. 
    #! 8) - Listado de todos los pokemones cuyo poder de pelea supere el valor promedio.
    #! 9) - el promedio de poder de todos los pokemones de tipo Psiquico.

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA - Pokedex")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text="Pokedex", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        # self.image = tk.PhotoImage(file='Logo_UTN_App.png')
        
        # self.top_banner = customtkinter.CTkLabel(master = self, image = self.image, text = 'Banner')
        # self.top_banner.grid_configure(row = 1, column = 0, padx = 20, pady = 5, columnspan = 2, rowspan = 1, sticky = 'we')

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Pokedex", command=self.btn_cargar_pokedex_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")
        self.btn_mostrar_todos = customtkinter.CTkButton(master=self, text="Mostrar todos", command=self.btn_mostrar_todos_on_click)
        self.btn_mostrar_todos.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_1 = customtkinter.CTkButton(master=self, text="Informe 1", command=self.btn_mostrar_informe_1)
        self.btn_informe_1.grid(row=4, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_2 = customtkinter.CTkButton(master=self, text="Informe 2", command=self.btn_mostrar_informe_2)
        self.btn_informe_2.grid(row=5, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_3 = customtkinter.CTkButton(master=self, text="Informe 3", command=self.btn_mostrar_informe_3)
        self.btn_informe_3.grid(row=6, pady=10, columnspan=2, sticky="nsew")
        # Cargar aca los pokemones
        self.lista_nombre_pokemones =["Squirtle", "Psyduck", "Cloyster", "Charmander", "Drowzee", "Gyarados", "Squirtle", "Mewtwo", "Charizard", "Magikarp"]
        self.lista_poder_pokemones = [90, 150, 150, 95, 70, 90, 150, 80, 50, 103]
        self.lista_tipo_pokemones = ["agua", "psíquico", "agua", "fuego", "psíquico", "agua", "agua", "psíquico", "fuego", "agua"]

    def btn_mostrar_todos_on_click(self):
        print("Index | Nombre     | tipo    | poder")        
        for i in range(len(self.lista_nombre_pokemones)):
            print(f"  {i}   | {self.lista_nombre_pokemones[i].rstrip()}    | {self.lista_tipo_pokemones[i]}  | {self.lista_poder_pokemones[i]}")
    
    def btn_mostrar_informe_1(self):
        # 4) - Porcentaje de pokemones de tipo agua con mas de 100 puntos de poder (Sobre el total de pokemones ingresados).
        total_pokemons = len(self.lista_nombre_pokemones)
        contador_poke_agua = 0
        for i in range(len(self.lista_nombre_pokemones)):
            if self.lista_tipo_pokemones[i] == "agua" and self.lista_poder_pokemones[i] > 100:
                contador_poke_agua += 1
                
        porcentaje = (contador_poke_agua * 100) / total_pokemons
        print(f"El porcentaje de pokemons de agua con mas de 100 de poder es: {porcentaje}%")

    def btn_mostrar_informe_2(self):
        # 5) - Porcentaje de pokemones de tipo psiquico con poder de pelea inferior o igual a 150 (sobre el total de pokemones ingresados).
        total_pokemons = len(self.lista_nombre_pokemones)
        contador_poke_psiquico = 0
        for i in range(len(self.lista_nombre_pokemones)):
            if self.lista_tipo_pokemones[i] == "psíquico" and self.lista_poder_pokemones[i] <= 150:
                contador_poke_psiquico += 1

        porcentaje = (contador_poke_psiquico * 100) / total_pokemons
        print(f"El porcentaje de pokemons psíquico con menos de 100 de poder es: {porcentaje}%")
        
    def btn_mostrar_informe_3(self):
        # 9) - el promedio de poder de todos los pokemones de tipo Psiquico.
        contador = 0
        suma_poder = 0
        for i in range(len(self.lista_nombre_pokemones)):
            if self.lista_tipo_pokemones[i] == "psíquico":       
                suma_poder += self.lista_poder_pokemones[i]
                contador += 1
                
        promedio = suma_poder / contador
        print(f"El promedio de poder de pokemons tipo psíquico es: {promedio}")

        
        
                
    def btn_cargar_pokedex_on_click(self):
        for i in range(10):
            
            while True:
                nombre = prompt("UTN",f"Ingrese nombre ({i})")
                if nombre != None and nombre != "":
                    self.lista_nombre_pokemones.append(nombre)
                    break
            
            while True:
                tipo = prompt("UTN","Ingrese tipo\n(Agua, Psíquico, Fuego)")
                # AGUA  
                if tipo != None and tipo != "":
                    tipo = tipo.lower()
                    #agua
                    if tipo == "agua" or tipo == "psiquico" or tipo == "fuego" :
                        self.lista_tipo_pokemones.append(tipo)
                        break
                
            while True:
                poder = prompt("UTN","Ingrese poder")
                if poder != None and poder != "":
                    poder = int(poder)
                    if poder >= 50 and poder <= 200:
                        self.lista_poder_pokemones.append(poder)
                        break
            
            respuesta = question("UTN","desea continuar?")
            if not respuesta:
                break
        
        
        
        
        
if __name__ == "__main__":
    app = App()
    print("La app esta funcionando")
    app.mainloop()
    
    '''
    # 0) - Cantidad de pokemones de tipo Fuego cuyo poder de pelea con un 10% extra supere los 100 puntos.
        contador = 0
        for i in range(len(self.lista_nombre_pokemones)):
            if self.lista_tipo_pokemones[i] == "fuego":
                poder_poke = self.lista_poder_pokemones[i] +( self.lista_poder_pokemones[i] * 0.1)
                if poder_poke > 100: 
                    contador += 1
        print(f"La cantidad de pokemons fuego con mas de 100 de poder son: {contador}")
        
    # 1) - Cantidad de pokemones de tipo Psiquico cuyo poder de pelea con un 15% menos este entre los 100 y los 150 puntos.
        contador_poke = 0
        for i in range(len(self.lista_nombre_pokemones)):
            if self.lista_tipo_pokemones[i] == "psíquico":
                poder_pokemon = self.lista_poder_pokemones[i] * 0.85
                if poder_pokemon >= 100 and poder_pokemon <= 150:
                    contador_poke += 1
        print(f"La cantidad de pokemons psiquico con su poder reducido por 15% que este entre 100 y 150 es: {contador_poke}")
    
    # 2) - Nombre y Poder del pokemon de tipo Agua con el poder mas alto.
        bandera_primero = True
        nombre_pokemon = None
        poder_pokemon =None
        for i in range(len(self.lista_nombre_pokemones)):
            if self.lista_tipo_pokemones[i] == "agua":
                if bandera_primero:
                    nombre_pokemon = self.lista_nombre_pokemones[i]
                    poder_pokemon = self.lista_poder_pokemones[i]
                    bandera_primero = False
                elif poder_pokemon < self.lista_poder_pokemones[i]:
                    nombre_pokemon = self.lista_nombre_pokemones[i]
                    poder_pokemon = self.lista_poder_pokemones[i]
        print(f"Nombre: {nombre_pokemon}\nPoder: {poder_pokemon}")
            
    # 3) - Nombre y Poder del pokemon de tipo Psiquico con el poder mas bajo.
        nombre_pokemon = None
        poder_pokemon = None
        for i in range(len(self.lista_nombre_pokemones)):
            if self.lista_tipo_pokemones[i] == "psíquico":
                if nombre_pokemon == None:
                    nombre_pokemon = self.lista_nombre_pokemones[i]
                    poder_pokemon = self.lista_poder_pokemones[i]
                elif poder_pokemon > self.lista_poder_pokemones[i]:
                    nombre_pokemon = self.lista_nombre_pokemones[i]
                    poder_pokemon = self.lista_poder_pokemones[i]
        print(f"Pokemon psíquico con menos poder es: \nNombre: {nombre_pokemon}\nPoder:{poder_pokemon}")
    
    # 6) - tipo de los pokemones del tipo que mas pokemones posea. 
        contador_fuego = 0
        contador_agua = 0
        contador_psiquico =0
        tipo_pokemon = None
        for i in range(len(self.lista_nombre_pokemones)):
            match self.lista_tipo_pokemones[i]:
                case "fuego":
                    contador_fuego += 1
                case "agua":
                    contador_agua += 1
                case "psiquico":
                    contador_psiquico += 1
        if contador_fuego > contador_agua and contador_fuego > contador_psiquico:
            tipo_pokemon = "fuego"
        elif contador_agua > contador_fuego and contador_agua > contador_psiquico:
            tipo_pokemon = "agua"
        else:
            tipo_pokemon = "psiquico"
        print(f"El tipo que mas pokemons tiene es: {tipo_pokemon}")
        
    # 7) - tipo de los pokemones del tipo que menos pokemones posea. 
        contador_fuego = 0
        contador_agua = 0
        contador_psiquico =0
        tipo_pokemon = None
        for i in range(len(self.lista_nombre_pokemones)):
            match self.lista_tipo_pokemones[i]:
                case "fuego":
                    contador_fuego += 1
                case "agua":
                    contador_agua += 1
                case "psíquico":
                    contador_psiquico += 1
        if contador_fuego < contador_agua and contador_fuego < contador_psiquico:
            tipo_pokemon = "fuego"
        elif contador_agua < contador_fuego and contador_agua < contador_psiquico:
            tipo_pokemon = "agua"
        else:
            tipo_pokemon = "psíquico"
        print(f"fuego: {contador_fuego} agua: {contador_agua} psiquico: {contador_psiquico}")
        print(f"El tipo que mas pokemons tiene es: {tipo_pokemon}")
        
    # 8) - Listado de todos los pokemones cuyo poder de pelea supere el valor promedio.
        cantidad_pokemons = len(self.lista_nombre_pokemones)
        suma_poder = 0
        for i in range(len(self.lista_nombre_pokemones)):
            suma_poder += self.lista_poder_pokemones[i]
            
        promedio_poder = suma_poder / cantidad_pokemons
        print(f"El promedio de poder es: {promedio_poder}")
        
        for i in range(len(self.lista_nombre_pokemones)):
            if self.lista_poder_pokemones[i] > promedio_poder:
                print(f"Nombre: {self.lista_nombre_pokemones[i]} \nTipo: {self.lista_tipo_pokemones[i]}\nPoder: {self.lista_poder_pokemones[i]}")
                print("----------")
    
    # 9) - el promedio de poder de todos los pokemones de tipo Psiquico.
        contador = 0
        suma_poder = 0
        for i in range(len(self.lista_nombre_pokemones)):
            if self.lista_tipo_pokemones[i] == "psíquico":       
                suma_poder += self.lista_poder_pokemones[i]
                contador += 1
                
        promedio = suma_poder / contador
        print(f"El promedio de poder de pokemons tipo psíquico es: {promedio}")
        
    '''