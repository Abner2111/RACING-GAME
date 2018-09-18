from tkinter import *
import tkinter
import random
from threading import Thread
import threading
import time
import os
import winsound
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
def Game():
    nombre = str(E_nombre.get())
    Juego(nombre)


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

#Entrada de texto para nombre del jugador
L_nombre = Label(C_main, text="Ingrese su nombre", font=("bauhaus 93", 18), width=27, bg="#DED7DE")
L_nombre.place(x=465, y=210)
E_nombre = Entry(C_main, text="Ingrese su nombre", width=59, bg="#DED7DE", fg="black")
E_nombre.place(x=465, y=260)

Titulo.place(y=0, x=0)

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
    ruta = os.path.join('img',"Foto.gif")
    img_foto = imagen=PhotoImage(file=ruta)
    foto = Label(C_about, image=img_foto)
    foto.photo = img_foto
    foto.place(y=50, x=700)
    #Botón de salir
    Salir = ttk.Button(C_about, text="SALIR", command=lambda: Main(about))
    Salir.place(x=1198, y=690)

def Juego(nombre):
    root.withdraw()
    #ventana principal del juego
    juego = Toplevel()
    juego.minsize(1280, 720)
    juego.resizable(width=NO, height=NO)

    #canvas principal
    C_main = Canvas(juego, bg="red", width=1280, height=720, borderwidth=0, highlightthickness=0)
    C_main.place(y=0, x=0)

    background = cargarImg("back.gif")
    fondo = Label(C_main, image=background, borderwidth=0)
    fondo.place(x=0, y=0)
    fondo.photo = background

    #Variable global de Velocidad del auto
    global speed
    speed = 1

    #canvas en que se desarrolla el juego
    C_game = Canvas(juego, bg="#DED7DE", width=1280/3, height=540, borderwidth=0, highlightthickness=0)
    C_game.place(x=1280/3, y=0)
    #labels del nombre del jugador
    L_name = Label(juego, text="Piloto :", font=("bauhaus 93", 18), width=10, justify="left", bg="#DED7DE", borderwidth=2, relief = "solid" )
    L_name.place(x=1280/12*8+50, y=100)

    V_name = Label(juego, text=nombre, font=("bauhaus 93", 18), bg="#DED7DE", borderwidth=2, relief = "solid")
    V_name.place(x=(1280/12*8)+185, y=100)

    #Carro del jugador
    img_carro = cargarImg("carro.gif")
    carro = C_game.create_image(215, 500, anchor=CENTER, image=img_carro)
    V_name.photo = img_carro

    #barras laterales
    left_line = C_game.create_rectangle((0, 0, 110/6, 540), fill="black")
    right_line = C_game.create_rectangle((390+110/6, 0, 1280/3, 540), fill="black")

    #Referencias
    left_reference = C_game.create_rectangle((0, 0, 110/6, 110/6), fill="white")
    right_reference = C_game.create_rectangle((390+110/6, 0, 1280/3, 110 / 6), fill="white")



    #Cantidad de Competidoes en pantalla

    #acelerar
    def acelerar():
        global speed
        speed = speed + 1


    #mueve referencias
    def move_refereces(speed):
        """
        mueve los elementos de la pantalla del juego de acuerdo a la velocidad definida
        :param speed:
        :return:
        """
        pos = C_game.coords(left_reference)
        C_game.move(left_reference, 0, speed)
        C_game.move(right_reference, 0, speed)

        if pos[3] >= 540:
            C_game.move(right_reference, 0, -(550-110/6))
            C_game.move(left_reference, 0, -(550 - 110 / 6))


    def derecha():
        """
        Mueve el carro hacia la derecha,
         si este no está en el borde derecho
        """
        if C_game.coords(carro)[0] < 345:
            C_game.move(carro, 130, 0)

    def izquierda():
        """
        Mueve el carro hacia la izquierda,
        si este no está en el borde izquierdo
        """
        if C_game.coords(carro)[0] > 85:
            C_game.move(carro, -130, 0)


    juego.bind("<Right>", lambda event: derecha())
    juego.bind("d", lambda event: derecha())
    juego.bind("<Left>", lambda event: izquierda())
    juego.bind("a", lambda event: izquierda())
    juego.bind("<Return>", lambda event: acelerar())
    #Botón de salir
    ttk.Button(C_main, text="SALIR", command = lambda : Main(juego)).place(x=1198, y=690)
    while True:
        move_refereces(speed)
        juego.update()
        time.sleep(0.1)





#BOTONES
img_play = cargarImg("play.gif")
img_about = cargarImg("info.gif")
play = Button(C_main, image=img_play, command=lambda : Game())
play.place(x=465, y=310)


about = Button(C_main, image=img_about, command=lambda: About())
about.place(y=630, x=1190)

#Binds Enter key to Game() function

root.bind("<Return>", lambda event: Game())

#MAINLOOP
root.mainloop()
