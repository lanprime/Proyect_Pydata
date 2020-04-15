import tkinter as tk
root = tk.Tk()
root.geometry('400x400')
root.title('Tiendita de frutas')

root.configure(bg="#009688")

mensaje = tk.StringVar()
boton = ""
def Menu():
    """Funcion que Muestra el Menu"""
    mensaje.set("""************
    Calculadora
    ************
    Menu
    1) Suma
    2) Resta
    3) Multiplicacion
    4) Division
    5) Salir""")
def Calculadora():
    """Funcion Para Calcular Operaciones Aritmeticas"""
    Menu()
    opc = int(input("Selecione Opcion\n"))
    while (opc >0 and opc <5):
        x = tk.StringVar()
        y = tk.StringVar()
        if (opc==1):
            print("La Suma es:", x+y)
            opc = int(input("Selecione Opcion\n"))
        elif(opc==2):
            print("La Resta es:",x-y)
            opc = int(input("Selecione Opcion\n"))
        elif(opc==3):
            print ("La Multiplicacion es:",x*y)
            opc = int(input("Selecione Opcion\n"))
        elif(opc==4):
            try:
              print("La Division es:", x/y)
              opc = int(input("Selecione Opcion\n"))
            except ZeroDivisionError:
              print("No se Permite la Division Entre 0")
              opc = int(input("Selecione Opcion\n"))

def digito(num):
    global boton
    boton = boton + str(num)
    calculo.set(boton)
def igual():
    try:
        global boton
        total = str(eval(boton))
        calculo.set(total)
        boton = ""
    except:
        calculo.set(" error ")
def limpiar():
    calculo.set("")
if __name__ == "__main__":
    calculo = tk.StringVar()
    Pantalla = tk.Entry(root ,font=("arial",20,"bold"),width =22,borderwidth =10, background= "Cyan",textvariable=calculo)
    Pantalla.place(x=20,y=60)
    Pantalla.grid(row=0, column =0, columnspan=4,padx =20,pady=20)
    #datos = Entry(ventana, textvariable=calculo)
    #datos.grid(columnspan=10, ipadx=50)
    boton1 = tk.Button(root, text=' 1 ', fg='black', bg='white',command=lambda: digito(1), height=2, width=5).grid(row=2, column=0,pady = 10)
    boton2 = tk.Button(root, text=' 2 ', fg='black', bg='white',command=lambda: digito(2), height=2, width=5).grid(row=2, column=1,pady = 10)
    boton3 = tk.Button(root, text=' 3 ', fg='black', bg='white',command=lambda: digito(3), height=2, width=5).grid(row=2, column=2,pady = 10)
    boton4 = tk.Button(root, text=' 4 ', fg='black', bg='white',command=lambda: digito(4), height=2, width=5).grid(row=3, column=0,pady = 10)
    boton5 = tk.Button(root, text=' 5 ', fg='black', bg='white',command=lambda: digito(5), height=2, width=5).grid(row=3, column=1,pady = 10)
    boton6 = tk.Button(root, text=' 6 ', fg='black', bg='white',command=lambda: digito(6), height=2, width=5).grid(row=3, column=2,pady = 10)
    boton7 = tk.Button(root, text=' 7 ', fg='black', bg='white',command=lambda: digito(7), height=2, width=5).grid(row=4, column=0,pady = 10)
    boton8 = tk.Button(root, text=' 8 ', fg='black', bg='white',command=lambda: digito(8), height=2, width=5).grid(row=4, column=1,pady = 10)
    boton9 = tk.Button(root, text=' 9 ', fg='black', bg='white',command=lambda: digito(9), height=2, width=5).grid(row=4, column=2,pady = 10)
    boton0 = tk.Button(root, text=' 0 ', fg='black', bg='white',command=lambda: digito(0), height=2, width=5).grid(row=5, column=0,pady = 10)

    suma = tk.Button(root, text=' + ', fg='black', bg='white',command=lambda: digito("+"), height=2, width=5).grid(row=2, column=3,pady = 10)
    resta = tk.Button(root, text=' - ', fg='black', bg='white',command=lambda: digito("-"), height=2, width=5).grid(row=3, column=3,pady = 10)
    multiplica = tk.Button(root, text=' * ', fg='black', bg='white',command=lambda: digito("*"), height=2, width=5).grid(row=4, column=3,pady = 10)
    divide = tk.Button(root, text=' / ', fg='black', bg='white',command=lambda: digito("/"), height=2, width=5).grid(row=5, column=3,pady = 10)
    resultado = tk.Button(root, text=' = ', fg='black', bg='white',command=igual, height=2, width=5).grid(row=5, column=2,pady = 10)
    limpiar = tk.Button(root, text='Limpiar', fg='black', bg='white',command=limpiar, height=2, width=5).grid(row=5, column='1',pady = 10)

    tk.Label(root, textvariable=mensaje, bg="#009688", fg='white', font=('', 24)).place(x=300, y=410)
    tk.Button(root, text='Salir', bd=0, command=root.destroy).grid(row=6,column=3,pady=10)
    root.mainloop()