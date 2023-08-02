import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Ezequiel
Apellido: Cura
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el
usuario quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    a. La suma acumulada de los negativos
    b. La suma acumulada de los positivos
    c. Cantidad de números positivos ingresados
    d. Cantidad de números negativos ingresados
    e. Cantidad de ceros
    f. El minimo de los negativos
    g. El maximo de los positivos
    h. El promedio de los negativos

Informar los resultados mediante alert()

'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_cargar = customtkinter.CTkButton(
            master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_cargar.grid(row=2, padx=20, pady=20,
                             columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar Estadísticas", command=self.btn_mostrar_estadisticas_on_click)
        self.btn_mostrar.grid(row=3, padx=20, pady=20,
                              columnspan=2, sticky="nsew")

        self.lista = []

    def btn_comenzar_ingreso_on_click(self):
        for _ in iter(int,1):
            num_ingresado = prompt("TP 08","Ingrese numero") 
            if num_ingresado != None and num_ingresado.isdigit():
               self.lista.append(int(num_ingresado)) 
            if num_ingresado != None and int(num_ingresado) < 0: # -asdf
                self.lista.append(int(num_ingresado))
            respuesta = question("Desea continuar?")
            if not respuesta:
                break 

    def btn_mostrar_estadisticas_on_click(self):
        suma_negativos = 0
        suma_positivos = 0
        contador_positivos = 0
        contador_negativos = 0
        contador_ceros = 0
        promedio_negativos = 0
        bandera = False
        minimo = 0
        maximo = 0
        # if len(self.lista) > 0:
        #     minimo = self.lista[0]
        #     maximo = self.lista[0]
            
        
        for i in self.lista:
            if i > 0:
                suma_positivos += i
                contador_positivos += 1
            elif i < 0: 
                suma_negativos += i
                contador_negativos += 1
            else:
                contador_ceros +=1
        
        for i in self.lista:
            if i > maximo:
                maximo = i
            elif i < minimo:
                minimo = i
            
            
        # minimo = min(self.lista)
        # maximo = max(self.lista)
        if contador_negativos != 0:             
            promedio_negativos = suma_negativos / contador_negativos
        
        
        alert("TP 08",f"Suma negativos:{suma_negativos}\nSuma positivos:{suma_positivos}\nCantidad numeros positivos:{contador_positivos}\nCantidad numeros negativos:{contador_negativos}\nCantidad ceros:{contador_ceros}\nMinimos y maximos:\n\tMinimo:{minimo}\n\tMaximo:{maximo}\nPromedio negativos:{promedio_negativos} ")
        
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
