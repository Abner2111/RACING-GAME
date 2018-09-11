from tkinter import *
import tkinter
from tkinter import messagebox
import random
from threading import Thread
import threading
import time
import os
#import winsound
from tkinter import ttk

#funcion para cargar imágenes
def cargarImg(nombre):
    ruta=os.path.join('img', nombre)
    imagen=PhotoImage(file=ruta)
    return imagen

#función para volver a la pantalla inicial
def Main(Window):
    Window.withdraw()
    root.deiconify()

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

    #Labels con informacion de About
    tec = Label(C_about, text="INSTITUTO TECNOLÓGICO DE COSTA RICA", bg="white", font = ("times new roman", 28))
    tec.place(y=0, x=25)
    carrera = Label(C_about, text="Carrera: Ingeniería en computadores", bg="white", font=("times new roman", 28))
    carrera.place(y=50, x=25)
    curso = Label(C_about, text="Curso: Taller de programación", bg="white", font=("times new roman", 28))
    curso.place(y=100, x=25)
    profesor = Label(C_about, text="Profesor: Milton Villegas Lemus", bg="white", font=("times new roman", 28))
    profesor.place(y=150, x=25)
    Dios = Label(C_about, text="Estudiante: Abner Arroyo Quesada", bg="white", font=("times new roman", 28))
    Dios.place(y=200, x=25)
    carnet = Label(C_about, text="Carnet: 2018103035", bg="white", font=("times new roman", 28))
    version = Label(C_about, text="Version: 1.0", bg="white", font=("times new roman", 28))
    ult_modc = Label(C_about, text="Última modificación: ND", bg="white", font=("times new roman", 28))
    ult_modc.place(y=250, x=25)
    img_foto = cargarImg("Foto.gif")
    foto = Label(C_about, image=img_foto, bg="white")
    foto.photo=img_foto
    foto.place(y=50, x=700)
    #Botón de salir
    Salir = ttk.Button(C_about, text="SALIR", command=lambda: Main(about))
    Salir.place(x=1198, y=690)

def Juego():
    return None



#BOTONES
img_play = cargarImg("play.gif")
img_about = cargarImg("info.gif")
play = Button(C_main, image=img_play)
play.place(x=465, y=310)

about = Button(C_main, image = img_about, command = lambda : About())
about.place(y = 630, x = 1190)

#MAINLOOP
root.mainloop()