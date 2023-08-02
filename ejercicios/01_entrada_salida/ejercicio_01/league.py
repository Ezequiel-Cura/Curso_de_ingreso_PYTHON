
import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Un jugador de League of Legends tiene un fin de semana libre y va a jugar partidas hasta que se canse.
Para mejorar su jugabilidad, por cada partida jugada va a registrar:
 - Modo de juego ("Normal", "Clasificatoria", "ARAM")
 - Nombre del personaje que usó
 - La cantidad de asesinatos (No puede ser negativo)
 - Muertes (No puede ser negativo)
 - Asistencias. (No puede ser negativo, hasta 40)

De lo registrado, al jugador le interesa lo siguiente:

a) El modo de juego más jugado.
b) El personaje con el cual murió más.
c) El promedio de asistencias.
d) De la partida con mas asesinatos, el nombre del personaje y el modo de juego.

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA - League of Legends")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text="League of Legends", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar datos", command=self.btn_cargar_datos_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")
        self.btn_mostrar_todos = customtkinter.CTkButton(master=self, text="Mostrar todos", command=self.btn_mostrar_todos_on_click)
        self.btn_mostrar_todos.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_1 = customtkinter.CTkButton(master=self, text="Informe 1", command=self.btn_mostrar_informe_1)
        self.btn_informe_1.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        # self.lista_modo_juego = []
        # self.lista_nombre_personaje = []
        # self.lista_cantidad_asesinatos = []
        # self.lista_muertes = []
        # self.lista_asistencias = []

        # - Modo de juego ("Normal", "Clasificatoria", "ARAM")
        self.lista_modo_juego = ["normal","clasificatoria","aram","aram","clasificatoria","normal","clasificatoria","normal","normal","clasificatoria"]
        # - Nombre del personaje que usó   
        self.lista_nombre_personaje = ["Ahri","Zoe","Zac","Ashe","Varus","Zed","Pyke","Gnar","Shen","Alistar"]
        # - La cantidad de asesinatos (No puede ser negativo)
        self.lista_cantidad_asesinatos = [20,34,50,10,9,43,12,1,2,5]
        # - Muertes (No puede ser negativo)
        self.lista_muertes = [10,23,3,2,6,15,1,4,5,9]
        # - Asistencias. (No puede ser negativo, hasta 40)
        self.lista_asistencias = [12,30,18,3,7,28,21,4,14,35]

    def btn_cargar_datos_on_click(self):
        for _ in iter(int,1):
            
            while True:
                modo_juego = prompt("Modo de juego UTN","Ingrese modo juego\n(Normal, Clasificatoria, ARAM)")
                modo_juego = modo_juego.lower()
                if modo_juego == "cormal" or modo_juego == "clasificatoria" or modo_juego == "aram":
                    self.lista_modo_juego.append(modo_juego)
                    break

            while True:
                nombre_personaje = prompt("Nombre personaje","Ingrese nombre del personaje")
                if nombre_personaje != None and nombre_personaje != "":
                    self.lista_nombre_personaje.append(nombre_personaje)                    
                    break
            
            while True: 
                cantidad_asesinatos = prompt("Cantidad asesinatos","Ingrese cantidad de asesinatos")
                if cantidad_asesinatos != None and cantidad_asesinatos != "":
                    cantidad_asesinatos = int(cantidad_asesinatos)
                    if cantidad_asesinatos >= 0:
                        self.lista_cantidad_asesinatos.append(cantidad_asesinatos)
                        break
                
            while True:
                muertes = prompt("Muertes","Cantidad de muertes")
                if muertes != None and muertes != "":
                    muertes = int(muertes)
                    if muertes >= 0:
                        self.lista_muertes.append(muertes)
                        break
            
            while True:
                asistencias = prompt("Asistencias","Cantidad de asistencias")
                if asistencias != None and asistencias != "":
                    asistencias = int(asistencias)
                    if asistencias >= 0 and asistencias <= 40:
                        self.lista_asistencias.append(asistencias)                        
                        break
            
            respuesta = question("pregunta", "Desea continuar?")
            if not respuesta: 
                break
                        
            
    def btn_mostrar_todos_on_click(self):
    # d) De la partida con mas asesinatos, el nombre del personaje y el modo de juego.
        nombre = None
        modo_juego = None
        mas_kills = None
       
        for i in range(len(self.lista_asistencias)):
            if mas_kills == None or self.lista_cantidad_asesinatos[i] > mas_kills:
                mas_kills = self.lista_cantidad_asesinatos[i]
                modo_juego = self.lista_modo_juego[i]
                nombre = self.lista_nombre_personaje[i]

        print(f"asesinatos: {mas_kills}, nombre: {nombre}, modo de juego: {modo_juego}")

    def btn_mostrar_informe_1(self):
    # c) El promedio de asistencias.
        suma = 0
        for assist in self.lista_asistencias:
            suma += assist
        
        promedio = suma / len(self.lista_asistencias)
        
        print(f"El promedio de asistencias es: {promedio}")
        
if __name__ == "__main__":
    app = App()
    print("La app esta funcionando")
    app.mainloop()
    
    
    '''
    # a) El modo de juego más jugado. ("Normal", "Clasificatoria", "ARAM")        
        contador_normal = 0
        contador_clasificatoria = 0
        contador_aram = 0
        mensaje = ""
        for i in self.lista_modo_juego:
            match i:
                case "normal":
                    contador_normal += 1
                case "clasificatoria":
                    contador_clasificatoria += 1
                case "aram":
                    contador_aram += 1
        
        if contador_normal > contador_clasificatoria and contador_normal > contador_aram:
            mensaje = "El modo de juego mas jugado es normal"
        elif contador_clasificatoria > contador_normal and contador_clasificatoria > contador_aram:
            mensaje = "El modo de juego mas jugado es clasificatoria"
        else:
            mensaje = "El modo de juego mas jugado es aram"
        print(f"Normal: {contador_normal}\nClasificatoria: {contador_clasificatoria}\naram: {contador_aram}")
        print(mensaje)

        
    # b) El personaje con el cual murió más.
        maximo = None # 10
        index = None # 0
        nombre = ""
        bandera = True
        for i in range(len(self.lista_cantidad_asesinatos)):
            if bandera == True:
                maximo = self.lista_muertes[i]
                index = i
                nombre = self.lista_nombre_personaje[i]
                bandera = False
            if maximo < self.lista_muertes[i]:
                maximo = self.lista_muertes[i]
                nombre = self.lista_nombre_personaje[i]
                index = i
                
        print(f"El personaje con mas muertes es {nombre}")
                                # self.lista_nombre_personaje[index]
    '''