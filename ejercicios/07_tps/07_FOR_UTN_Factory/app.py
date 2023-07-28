import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
'''
Nombre: Ezequiel
Apellido: Cura
Entregado
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

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
        cant_postulante_nb_ssr_net_jr = 0
        nombre_post_jr_menor_edad = ""
        edad_post_jr_menor_edad = None
        suma_edad_f = 0
        promedio_edad_f = 0
        
        suma_edad_m = 0     
        promedio_edad_m = 0
        
        suma_edad_nb = 0
        promedio_edad_nb = 0
        
        tecnologia_mas_postulantes = ""
        cant_python = 0
        cant_js = 0
        cant_net = 0
        cantidades_tecnologia = []
        
        cantidad_f = 0
        cantidad_m = 0
        cantidad_nb = 0
        
        for j in range(10):       
            
            # nombre = prompt("UTN","Ingrese nombre 2")
            # while nombre == None or nombre == "":
            #     nombre = prompt("UTN","Ingrese nombre 2")

            for i in range(100):
                nombre = prompt("UTN",f"Ingrese nombre {j}")
                if nombre != None and nombre != "":
                    break
            
            for i in range(100):
                edad = prompt("UTN","Ingrese edad")
                if edad != None and edad != "":
                    if edad.isdigit():
                        edad = int(edad)
                        if edad >= 18:
                            break
            
            for i in range(100):
                genero = prompt("UTN","Ingrese genero \n(F, M, NB)")
                if genero == "F" or genero == "M" or genero == "NB":
                    break
                
            for i in range(100):
                tecnologia = prompt("UTN","Ingrese tecnologia \n(PYTHON - JS - ASP.NET)")
                if tecnologia == "PYTHON" or tecnologia == "JS" or tecnologia == "ASP.NET":
                    break
                
            for i in range(100):
                puesto = prompt("UTN","Ingrese puesto \n(Jr - Ssr - Sr)")
                if puesto == "Jr" or puesto == "Ssr" or puesto == "Sr":
                    break
                
            
            #a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
            if genero == "NB" and (tecnologia == "ASP.NET" or tecnologia == "JS") and edad > 25 and edad < 40 and puesto == "Ssr":
                cant_postulante_nb_ssr_net_jr += 1
            #b. Nombre del postulante Jr con menor edad.
            if i == 0:
                nombre_post_jr_menor_edad = nombre
                edad_post_jr_menor_edad = edad
            if tecnologia == "Jr" and edad < edad_post_jr_menor_edad :
                nombre_post_jr_menor_edad = nombre
                edad_post_jr_menor_edad = edad
            #c. Promedio de edades por género.
            match genero:
                case "F":
                    suma_edad_f += edad
                    cantidad_f += 1
                case "M":
                    suma_edad_m += edad
                    cantidad_m += 1
                case "NB":
                    suma_edad_nb += edad
                    cantidad_nb += 1
            #d. Tecnologia con mas postulantes (solo hay una).    
            match tecnologia:
                case "PYTHON":
                    cant_python += 1
                case "JS":
                    cant_js += 1
                case "ASP.NET":
                    cant_net += 1
                    
        #SALIMOS DEL FOR
        #c. Promedio de edades por género.
        promedio_edad_f = suma_edad_f / cantidad_f
        promedio_edad_m = suma_edad_m / cantidad_m
        promedio_edad_nb = suma_edad_nb / cantidad_nb
        #d. Tecnologia con mas postulantes (solo hay una).    
        cantidades_tecnologia.append(cant_python)
        cantidades_tecnologia.append(cant_js)
        cantidades_tecnologia.append(cant_net)
        maximo = max(cantidades_tecnologia)
        if maximo == cant_python:
            tecnologia_mas_postulantes = "PYTHON"
        if maximo == cant_js:
            tecnologia_mas_postulantes = "JS"
        if maximo == cant_net:
            tecnologia_mas_postulantes = "ASP.NET"
        #e. Porcentaje de postulantes de cada genero.
        porcentaje_f = (cantidad_f * 10) / 100
        porcentaje_m = (cantidad_m * 10) / 100
        porcentaje_nb = (cantidad_nb * 10) / 100
        
        print(f"Cantidad de postulantes NB, ASP.NET o JS, de edad entre 25 a 40, con puesto Ssr: {cant_postulante_nb_ssr_net_jr} \nNombre postulante con menor edad: {nombre_post_jr_menor_edad}\nPromedio de edades por genero:\n \tF= {promedio_edad_f},\n \tM= {promedio_edad_m},\n \tNB= {promedio_edad_nb}\nTecnologia con mas postulantes: {tecnologia_mas_postulantes}\nPorcentaje de postulantes por genero:\n \tF:{porcentaje_f}%\n \tM:{porcentaje_m}%\n \tNB:{porcentaje_nb}%")
        
        
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
