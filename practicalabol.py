from tkinter import *

root=Tk()

miFrame=Frame(width=1200,height=600)
miFrame.pack()

cuadroDNI=Entry(miFrame)
cuadroDNI.grid(row=0, column=1)

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1, column=1)

cuadroDirección=Entry(miFrame)
cuadroDirección.grid(row=2, column=1)

cuadroTeléfono=Entry(miFrame)
cuadroTeléfono.grid(row=3, column=1)

DNILabel=Label(miFrame, text="DNI:")
DNILabel.grid(row=0, column=0)

ApellidoLabel=Label(miFrame, text="Apellido:")
ApellidoLabel.grid(row=1, column=0)

DirecciónLabel=Label(miFrame, text="Dirección:")
DirecciónLabel.grid(row=2, column=0)

TeléfonoLabel=Label(miFrame, text="Teléfono:")
TeléfonoLabel.grid(row=3, column=0)

root.mainloop()
