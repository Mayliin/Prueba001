from tkinter import *
w = Tk()

l = Label(w, text='Etiqueta')
l.pack() #empaca dentro del contenedor

b = Button(w, text='Boton')
b.pack() #empaca dentro del contenedor

e = Entry(w)
e.pack() #empaca dentro del contenedor

w.mainloop()
