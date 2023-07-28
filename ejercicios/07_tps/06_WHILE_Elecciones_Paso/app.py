import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
Nombre: Ezequiel
Apellido: Cura
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por consola (print)

'''
class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        total_votos = 0
        nombre_candidato_con_mas_votos = ""
        nombre_candidato_con_menos_votos = ""
        edad_candidato_con_menos_votos = ""
        promedio_edades = 0
        suma_edades = 0
        voto_candidato = 0
        contador = 0
        
        
        while True:
            
            while True:
                nombre = prompt("EJ TP06","ingrese un nombre")
                if nombre != "" and nombre != None:
                    if contador == 0:
                        nombre_candidato_con_mas_votos = nombre
                        nombre_candidato_con_menos_votos = nombre
                    break
            
            while True: 
                edad = prompt("EJ TP06","Ingrese edad")
                if edad != None and edad.isdigit() and int(edad) > 25 :
                    if contador == 0:
                        edad_candidato_con_menos_votos = edad
                    suma_edades += edad
                    break 
            
            while True:
                votos = prompt("EJ TP06","Ingrese votos")
                if votos != "" and votos != None and votos.isdigit() and int(votos) > 0:
                    if total_votos == 0:
                        voto_candidato = votos
                    if votos > voto_candidato:
                        voto_candidato = votos
                        nombre_candidato_con_mas_votos = nombre
                    
                    total_votos += votos                    
                    break
            
            
            contador += 1
            
            respuesta = question("UTN","Desea continuar?")
            if respuesta:
                break        
            '''    
            a. nombre del candidato con más votos
            b. nombre y edad del candidato con menos votos
            c. el promedio de edades de los candidatos
            d. total de votos emitidos.
            Todos los datos se ingresan por prompt y los resultados por consola (print)
            '''
        
        promedio_edades = suma_edades / contador
        
        
        
        print("El candidato con mas votos es: {nombre_candidato_con_mas_votos}  \n El candidato con menos votos es: {nombre_candidato_con_menos_votos} y edad: {edad_candidato_con_menos_votos} \nPromedio de edades entre candidatos: {promedio_edades} \n Total de votos emitidos:{total_votos} ")
        
        

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
