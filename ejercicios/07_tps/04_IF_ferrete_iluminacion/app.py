import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Ezequiel
Apellido: Cura

Todas las lámparas están  al mismo precio de $800 pesos final.
Entregado		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
Entregado		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
Entregado		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
Entregado		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
Entregado		E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        # configure window
        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
        cantidad = int(self.combobox_cantidad.get())
        marca = self.combobox_marca.get()
        importe = cantidad * 800
        importe_descuento = importe
        if cantidad >= 6:
            importe_descuento = importe/2    #50%
        elif cantidad == 5:
            if marca == "ArgentinaLuz":
                importe_descuento = importe - ( importe * 0.4)#40%
            else:
                importe_descuento =  importe - ( importe * 0.3)#30%
        elif cantidad == 4:
            if marca == "ArgentinaLuz" or marca == "FelipeLamparas":
                importe_descuento = importe - ( importe * 0.25)#25%
            else:
                importe_descuento= importe - ( importe * 0.20)#20%
        elif cantidad == 3:
            if marca == "ArgentinaLuz":
                importe_descuento = importe - ( importe * 0.15)#15%
            elif marca == "FelipeLamparas":
                importe_descuento =  importe - ( importe * 0.10)#10%
            else:
                importe_descuento =  importe - ( importe * 0.05)#5%
        
        if importe_descuento >= 4000:
            importe_descuento =  importe_descuento - ( importe_descuento * 0.05)# un adicional 5%
        
        alert("Ej TP_04_IF",f"Tu importe final es de {importe_descuento}")

    
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()