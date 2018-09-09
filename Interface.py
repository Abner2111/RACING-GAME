from tkinter import *
import tkinter
from tkinter import messagebox
import random
from threading import Thread
import threading
import time
import os
import winsound
from tkinter import ttk

def cargarImg(nombre):
    ruta=os.path.join('img',nombre)
    imagen=PhotoImage(file=ruta)
    return imagen

#Ventana principal
root = Tk()
root.title("Racing Game")
root.minsize(1280, 720)
root.resizable(height=NO, width=NO)
#Canvas principal
C_main = Canvas(root, bg="#DED7DE", width=1280, height=720)
C_main.place(x=0, y=0)

#Titulo
img_titulo = cargarImg("titulo.gif")
Titulo = Label(C_main,image=img_titulo, bg="white"\
               , borderwidth=0, highlightthickness=0)

Titulo.place(y=0,x=0)

def About():
    root.withdraw()
    about = Toplevel()
    about.title("About the developer")
    about.minsize(1280, 720)
    about.resizable(width=NO, height=NO)

    C_about = Label(about, bg="white", width=1280, height=720)
    C_about.place(x=0,y=0)

    tec = Label(C_about, text="INSTITUTO TECNOLÓGICO DE COSTA RICA", bg="white", font = ("times new roman", 28)).place(y=0,x=50)
    Salir = ttk.Button(C_about, text="SALIR", command = lambda :Main(about))




def Main(Window):
    Window.withdraw()
    root.deiconify()

#BOTONES
img_play = cargarImg("play.gif")
img_about = cargarImg("info.gif")
play = Button(C_main, image = img_play)
play.place(x=465, y=310)

about = Button(C_main, image = img_about, command = lambda : About())
about.place(y = 630, x = 1190)

#MAINLOOP
root.mainloop()