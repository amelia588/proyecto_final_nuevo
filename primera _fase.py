#Aplicaion para fereteria "El Tornillo Feliz" 
from tkinter import *


raiz=Tk()

raiz.title("ventana de pruebas")

#raiz.resizable(True,False)

raiz.iconbitmap("C:\proyecto_4\hrian.ico")

#raiz.geometry("650x350")

raiz.config(bg="pink")

raiz.config(bd=45)

raiz.config(relief="groove")

raiz.config(cursor="hand2")

miFrame=Frame()

miFrame.pack(fill="y")

miFrame.config(bg="yellow")

miFrame.config(width="650",height="350")

miFrame.config(bd=35)

miFrame.config(relief="sunken")

raiz.mainloop()