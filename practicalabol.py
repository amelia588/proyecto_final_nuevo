from tkinter import *

root=Tk()

miFrame=Frame(width=1200,height=600)
miFrame.pack()

cuadroDNI=Entry(miFrame)
cuadroDNI.grid(row=0, column=1, padx=10, pady=10)

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1, column=1, padx=10, pady=10)

cuadroDirección=Entry(miFrame)
cuadroDirección.grid(row=2, column=1, padx=10, pady=10)

cuadroTeléfono=Entry(miFrame)
cuadroTeléfono.grid(row=3, column=1, padx=10, pady=10)

DNILabel=Label(miFrame, text="DNI:")
DNILabel.grid(row=0, column=0, sticky="w", padx=10, pady=10)

ApellidoLabel=Label(miFrame, text="Apellido:")
ApellidoLabel.grid(row=1, column=0, sticky="w", padx=10, pady=10)

DirecciónLabel=Label(miFrame, text="Dirección:")
DirecciónLabel.grid(row=2, column=0, sticky="w", padx=10, pady=10)

TeléfonoLabel=Label(miFrame, text="Teléfono:")
TeléfonoLabel.grid(row=3, column=0, sticky="w", padx=10, pady=10)

root.mainloop()
