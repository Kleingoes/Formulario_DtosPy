
import tkinter as tk
from tkinter import messagebox
import re

def guardar_datos():
    #Obtener los datos de los campos
    nombres = entry_nombres.get()
    apellidos = entry_apellidos.get()
    edad = entry_edad.get()
    estatura = entry_estatura.get()
    telefono = entry_telefono.get()

    #obtener el genero selecionado 
    genero =""
    if var_genero.get() ==1:
        genero ="Hombre"
    elif var_genero.get()==2:
        genero = "Mujer"

    #Validar los campos tengan el formato correcto 
    if (es_entero_valido(edad) and es_decimal_valido(estatura) and es_entero_valido_de_10_digitos(telefono) and es_texto_valido(nombres) and es_texto_valido(apellidos)):
        datos = f"Nombres: {nombres} \n Apellidos: {apellidos} \n Edad: {edad} \n Estatura: {estatura}\n Telefono: {telefono} \n Genero: {genero}"

        #Guardar los datos en un archivo de texto
        with open ("PruebaVentana.text", "a") as archivo:
            archivo.write(datos + "\n\n")

        #Mostrar un mensaje con los datos capturados 
        messagebox.showinfo("imformacion","Datos guardados con exito:\n\n"+ datos)

        #Limpiar los controles despues de guardar 
        limpiar_campos()
    else:
        messagebox.showerror("Error","Por favor, ingre datos validos en los campos.")

def limpiar_campos():
    entry_nombres.delete(0,tk.END)
    entry_apellidos.delete(0,tk.END)
    entry_edad.delete(0,tk.END)
    entry_estatura.delete(0,tk.END)
    entry_telefono.delete(0,tk.END)
    var_genero.set(0)

def es_entero_valido(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False

def es_decimal_valido(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

def es_entero_valido_de_10_digitos(valor):
    return valor.isdigit() and len(valor) == 10

def es_texto_valido(valor):
    return bool(re.match("^[a-zA-Z\s]+$",valor))

#Crear la ventana principal
ventana = tk.Tk()
ventana.title("Formulario")

#Crear variables para los radio buttons 
var_genero= tk.IntVar()

#Crear etiquetas y campos de netranda
label_nombres = tk.Label(ventana, text="Nombres: ")
label_nombres.pack()
entry_nombres =tk.Entry(ventana)
entry_nombres.pack()

label_apellidos = tk.Label(ventana, text="apellidos")
label_apellidos.pack()
entry_apellidos = tk.Entry(ventana)
entry_apellidos.pack()

label_edad = tk.Label(ventana, text="Edad:")
label_edad.pack()
entry_edad = tk.Entry(ventana)
entry_edad.pack()

estatura_label = tk.Label(ventana, text= "Estatura: ")
estatura_label.pack()
entry_estatura = tk.Entry(ventana)
entry_estatura.pack()

label_telefono = tk.Label(ventana, text="Telefono:")
label_telefono.pack()
entry_telefono = tk.Entry(ventana)
entry_telefono.pack()

label_genero = tk.Label(ventana, text="Genero: ")
label_genero.pack()

rb_hombres = tk.Radiobutton(ventana, text="Hombre", variable = var_genero, value=1)
rb_hombres.pack()

rb_mujer = tk.Radiobutton(ventana, text="Mujer", variable = var_genero, value=2)
rb_mujer.pack()

btn_guardar =tk.Button(ventana, text="Guardar", command= guardar_datos)
btn_guardar.pack()

btn_limpiar = tk.Button(ventana, text="Limpiar",command= limpiar_campos)
btn_limpiar.pack()

#Iniciar la aplicacion
ventana.mainloop()