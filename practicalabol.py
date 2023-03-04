from tkinter import *

root=Tk()
root.title('Ferreteria el tornillo feliz')

miFrame=Frame(root)
miFrame.pack()

miFrame=Frame( root, width=1200, height=600)
miFrame.pack()

cuadroDNI=Entry(miFrame)
cuadroDNI.grid(row=0, column=1, padx=10, pady=10)
cuadroDNI.config(fg="blue")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1, column=1, padx=10, pady=10)

cuadroNombre=Entry(miFrame)
cuadroNombre.grid(row=1, column=3, padx=10, pady=10)

cuadroDirección=Entry(miFrame)
cuadroDirección.grid(row=2, column=1,columnspan=3,sticky="we",  padx=10, pady=10)

cuadroTeléfono=Entry(miFrame)
cuadroTeléfono.grid(row=3, column=1, columnspan=3,sticky="we", padx=10, pady=10)

DNILabel=Label(miFrame, text="DNI:")
DNILabel.grid(row=0, column=0, sticky="w", padx=10, pady=10)

ApellidoLabel=Label(miFrame, text="Apellido:")
ApellidoLabel.grid(row=1, column=0, sticky="w", padx=10, pady=10)

NombreLabel=Label(miFrame, text="Nombre:")
NombreLabel.grid(row=1, column=2, sticky="w", padx=10, pady=10)


DirecciónLabel=Label(miFrame, text="Dirección:")
DirecciónLabel.grid(row=2, column=0, sticky="w", padx=10, pady=10)

TeléfonoLabel=Label(miFrame, text="Teléfono:")
TeléfonoLabel.grid(row=3, column=0, sticky="w", padx=10, pady=10)


cod_prodLabel=Label(miFrame,text="cod_prod")
cod_prodLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

cod_prod=Entry(miFrame, width=7)
cod_prod.grid(row=5, column=0, padx=10, pady=10)

cod_prod=Entry(miFrame, width=7)
cod_prod.grid(row=6, column=0, padx=10, pady=10)

cod_prod=Entry(miFrame, width=7)
cod_prod.grid(row=7, column=0, padx=10, pady=10)

DescripciónLabel=Label(miFrame,text="Descripción")
DescripciónLabel.grid(row=4, column=1, sticky="ew", padx=10, pady=10)

Descripción=Entry(miFrame, width=7, state="readonly")
Descripción.grid(row=5, column=1, padx=10, pady=10)

Descripión=Entry(miFrame, width=7, state="readonly")
Descripión.grid(row=6, column=1, padx=10, pady=10)

Descripción=Entry(miFrame, width=7, state="readonly")
Descripción.grid(row=7, column=1, padx=10, pady=10)

UnidadLabel=Label(miFrame,text="Unidad")
UnidadLabel.grid(row=4, column=2, sticky="ew", padx=10, pady=10)

Unidad=Entry(miFrame, width=7, state="readonly")
Unidad.grid(row=5, column=2, padx=10, pady=10)

Unidad=Entry(miFrame, width=7, state="readonly")
Unidad.grid(row=6, column=2, padx=10, pady=10)

Unidad=Entry(miFrame, width=7, state="readonly")
Unidad.grid(row=7, column=2, padx=10, pady=10)

CantidadLabel=Label(miFrame,text="Cantidad")
CantidadLabel.grid(row=4, column=3, sticky="ew", padx=10, pady=10)

Cantidad=Entry(miFrame, width=7)
Cantidad.grid(row=5, column=3, padx=10, pady=10)

Cantidad=Entry(miFrame, width=7)
Cantidad.grid(row=6, column=3, padx=10, pady=10)

Cantidad=Entry(miFrame, width=7)
Cantidad.grid(row=7, column=3, padx=10, pady=10)

PrecioLabel=Label(miFrame,text="Precio")
PrecioLabel.grid(row=4, column=4, sticky="ew", padx=10, pady=10)

Precio=Entry(miFrame, width=7, state="readonly")
Precio.grid(row=5, column=4, padx=10, pady=10)

Precio=Entry(miFrame, width=7, state="readonly")
Precio.grid(row=6, column=4, padx=10, pady=10)

Precio=Entry(miFrame, width=7, state="readonly")
Precio.grid(row=7, column=4, padx=10, pady=10)

SubtotalLabel=Label(miFrame,text="Subtotal")
SubtotalLabel.grid(row=4, column=5, sticky="ew", padx=10, pady=10)

Subtotal=Entry(miFrame, width=7, state="readonly")
Subtotal.grid(row=5, column=5, padx=10, pady=10)

Subtotal=Entry(miFrame, width=7, state="readonly")
Subtotal.grid(row=6, column=5, padx=10, pady=10)

Subtotal=Entry(miFrame, width=7, state="readonly")
Subtotal.grid(row=7, column=5, padx=10, pady=10)

TotalLabel=Label(miFrame,text="Total")
TotalLabel.grid(row=7, column=6, sticky="ew", padx=10, pady=10)

Total=Entry(miFrame, width=7, state="readonly")
Total.grid(row=7, column=7, padx=10, pady=10)

Guardar=Button(miFrame, text="Guardar")
Guardar.grid(row=8, column=2, padx=10, pady=10)



root.mainloop()
