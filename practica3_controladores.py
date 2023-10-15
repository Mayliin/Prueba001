from tkinter import *
def saludar():
    print ('Hola')
w = Tk()

l = Label(w, text='Etiqueta')
l.pack() #empaca dentro del contenedor

b = Button(w, text='Saludar', command=saludar)
b.pack() #empaca dentro del contenedor

b2 = Button(w, text='Salir', command=exit)
b2.pack()

w.mainloop()