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

#BOTONES
img_play = cargarImg("play.gif")
play = ttk.Button(C_main, image = img_play)
play.place(x=465, y=310)
root.mainloop()