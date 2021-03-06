from tkinter import *
import tkinter
from tkinter import messagebox
import random
import time
import os
import winsound
from tkinter import ttk

# Cancion de inicio

def Start_song():
    winsound.PlaySound('sounds\\start.wav', winsound.SND_ASYNC)

# detener sonido
def off():
    winsound.PlaySound(None, winsound.SND_ASYNC)
# funcion para cargar imágenes
def cargarImg(nombre):
    ruta=os.path.join('img', nombre)
    imagen=PhotoImage(file=ruta)
    return imagen

# función para volver a la pantalla inicial
def Main(Window):
    Start_song()
    Window.destroy()
    root.deiconify()

def Game():
    off()
    nombre = str(E_nombre.get())
    Juego(nombre)


# Ventana principal
root = Tk()
root.title("Racing Game")
root.minsize(1280, 720)
root.resizable(height=NO, width=NO)
# Canvas principal
C_main = Canvas(root, bg="#DED7DE", width=1280, height=720)
C_main.place(x=0, y=0)

# Titulo
img_titulo = cargarImg("titulo.gif")
Titulo = Label(C_main, image=img_titulo, bg="white"
               , borderwidth=0, highlightthickness=0)

# Entrada de texto para nombre del jugador
L_nombre = Label(C_main, text="Ingrese su nombre", font=("bauhaus 93", 18), width=27, bg="#DED7DE")
L_nombre.place(x=465, y=210)
E_nombre = Entry(C_main, text="Ingrese su nombre", width=25, font=("bauhaus 93", 18), bg="#DED7DE", fg="black",
                 justify=CENTER)
E_nombre.place(x=465, y=260)

Start_song()

Titulo.place(y=0, x=0)

def About():
    off()
    root.withdraw()
    about = Toplevel()
    about.title("About the developer")
    about.minsize(1280, 720)
    about.resizable(width=NO, height=NO)

    C_about = Label(about, bg="white", width=1280, height=720)
    C_about.place(x=0,y=0)

#   Labels con informacion de About
    tec = Label(C_about, text="INSTITUTO TECNOLÓGICO DE COSTA RICA", bg="white", font = ("times new roman", 28))
    tec.place(y=0, x=25)
    carrera = Label(C_about, text="Carrera: Ingeniería en computadores", bg="white", font=("times new roman", 28))
    carrera.place(y=50, x=25)
    curso = Label(C_about, text="Curso: Taller de programación", bg="white", font=("times new roman", 28))
    curso.place(y=100, x=25)
    profesor = Label(C_about, text="Profesor: Milton Villegas Lemus", bg="white", font=("times new roman", 28))
    profesor.place(y=150, x=25)
    YO = Label(C_about, text="Estudiante: Abner Arroyo Quesada", bg="white", font=("times new roman", 28))
    YO.place(y=200, x=25)
    carnet = Label(C_about, text="Carnet: 2018103035", bg="white", font=("times new roman", 28))
    version = Label(C_about, text="Version: 1.0", bg="white", font=("times new roman", 28))
    ult_modc = Label(C_about, text="Última modificación: 21 / 9 / 2018", bg="white", font=("times new roman", 28))
    ult_modc.place(y=250, x=25)
    ruta = os.path.join('img',"Foto.gif")
    img_foto = imagen=PhotoImage(file=ruta)
    foto = Label(C_about, image=img_foto)
    foto.photo = img_foto
    foto.place(y=50, x=700)
#   Botón de salir
    Salir = ttk.Button(C_about, text="SALIR", command=lambda: Main(about))
    Salir.place(x=1198, y=690)

def Juego(nombre):

    root.withdraw()


#    Variable global de Velocidad del auto
    global speed, players, max_vel, ind_vel, gear, recorrido, rpm_i, recorrido_dato, C1, C2, img_carro, ind_gear, \
        min_vel, gear_lowered, deteniendo, rpm, ind_rpm, revasados, revasados_count
    revasados = IntVar()
    revasados_count = 0
    speed = 10
    players = 0
    max_vel = 15
    min_vel = 10
    gear = 1
    recorrido = IntVar()
    recorrido_dato = 0
    inicio = time.time()
    tiempo = StringVar()
    rpm_i = time.time()
    gear_lowered = False
    deteniendo = 0
    rpm = 0
    def pierde():
        reiniciar = messagebox.askyesno("Usted ha perdido", "Jugar de nuevo?")
        if reiniciar:
            Main(juego)
        else:
            root.destroy()
    def gana():
        reiniciar = messagebox.askyesno("Usted ha ganado", "Jugar de nuevo?")
        if reiniciar:
            Main(juego)
        else:
            root.destroy()

    def contar_tiempo():
        fin = time.time()
        tiempo.set(str(int(fin-inicio)))

#    #ventana principal del juego
    juego = Toplevel()
    juego.minsize(1280, 720)
    juego.resizable(width=NO, height=NO)

#   canvas principal
    C_main = Canvas(juego, bg="red", width=1280, height=720, borderwidth=0, highlightthickness=0)
    C_main.place(y=0, x=0)

#   fondo
    background = cargarImg("back.gif")
    fondo = Label(C_main, image=background, borderwidth=0)
    fondo.place(x=0, y=0)
    fondo.photo = background

#   labels del nombre del jugador
    L_name = Label(C_main, text="Piloto :", font=("bauhaus 93", 18), width=10, justify="left", bg="#DED7DE",
                   borderwidth=2, relief="solid")
    L_name.place(x=1280 / 12 * 8 + 50, y=100)
    V_name = Label(juego, text=nombre, font=("bauhaus 93", 18), bg="#DED7DE", borderwidth=2, relief="solid")
    V_name.place(x=(1280 / 12 * 8) + 185, y=100)


#   Label de tiempo
    N_tiempo = Label(C_main, text="TIEMPO DE JUEGO", font=("bauhaus 93", 18), width=15, justify="left", bg="#DED7DE",
                   borderwidth=2, relief="solid")
    N_tiempo.place(x=1280 / 12 + 50, y=65)
    L_tiempo = Label(C_main, textvariable=tiempo, font=("bauhaus 93", 18), width=15, justify="left", bg="#DED7DE",
                   borderwidth=2, relief="solid")
    L_tiempo.place(x=1280 / 12 + 50, y=100)

#   Label de recorrido
    N_recorrido = Label(C_main, text="KMs RECORRIDOS", width=15, font=("bauhaus 93", 18), justify="left",
                        bg="#DED7DE", borderwidth=2, relief="solid")
    N_recorrido.place(x=1280 / 12 + 50, y=215)
    L_recorrido = Label(C_main, textvariable=recorrido, font =("bauhaus 93", 18), width=15, justify="left",
                         bg="#DED7DE", borderwidth=2, relief="solid")
    L_recorrido.place(x=1280 / 12 + 50, y=250)

#   Canvas de estadisticas
    C_info = Canvas(juego, bg="#DED7DE", width=1280/3, height=180, borderwidth=0, highlightthickness=0)
    C_info.place(x=1280/3, y=540)



    dashboard = cargarImg("dash.gif")
    dash = C_info.create_image(213, 90, anchor=CENTER, image=dashboard)
    juego.photo = dashboard

#   Indicador de velocidad
    ind_vel = C_info.create_text(165, 50, text=str(speed), font=("segoe ui semibold", 20))
    km = C_info.create_text(165, 70, text="Km/h", font=("segoe ui semibold", 15))
#   Indicador de marchas
    ind_gear = C_info.create_text(253, 50, text=str(gear), font=("segoe ui semibold", 20))
    marcha = C_info.create_text(253, 70, text="Marcha", font=("segoe ui semibold", 15))
#   Indicador de RPM
    ind_rpm = C_info.create_text(328, 80, text=str(rpm), font=("segoe ui semibold", 20))
#   Canvas en que se desarrolla el juego
    C_game = Canvas(juego, bg="#DED7DE", width=1280/3, height=540, borderwidth=0, highlightthickness=0)
    C_game.place(x=1280/3, y=0)

#   Carro del jugador
    img_carro = cargarImg("carro.gif")
    carro = C_game.create_image(215, 500, anchor=CENTER, image=img_carro)
    juego.photo = img_carro

#   barras laterales
    left_line = C_game.create_rectangle((0, 0, 110/6, 540), fill="black")
    right_line = C_game.create_rectangle((390+110/6, 0, 1280/3, 540), fill="black")

#   Referencias
    left_reference = C_game.create_rectangle((0, 0, 110/6, 110/6), fill="white")
    right_reference = C_game.create_rectangle((390+110/6, 0, 1280/3, 110 / 6), fill="white")

    #   competidores
    img_compe = cargarImg("competidor.gif")
    C1 = C_game.create_image(85+(130*random.randint(0, 2)), 10, anchor=CENTER, image=img_compe)
    C2 = C_game.create_image(85+(130*random.randint(0, 2)), 10, anchor=CENTER, image=img_compe)
    juego.photo = img_compe

#   obliga a cambiar de marcha
    def make_chage():
        global rpm_i, rpm
        fin = time.time()
        rpm_tmp = fin - rpm_i
        if gear == 4:
            pass
        elif gear-1 < rpm_tmp < gear:
            winsound.PlaySound('sounds\\warning.wav', winsound.SND_ASYNC)
        elif rpm_tmp >= gear+1:
            pierde()
        rmp = int(rpm_tmp) * 1000
        update_stats()

    def update_stats():
        global ind_vel, ind_gear, ind_rpm
        C_info.delete(ind_vel)
        ind_vel = C_info.create_text(165, 50, text=str(speed), font=("segoe ui semibold", 20))
        C_info.delete(ind_gear)
        ind_gear = C_info.create_text(253, 50, text=str(gear), font=("segoe ui semibold", 20))
        C_info.delete(ind_rpm)
        ind_rpm = C_info.create_text(328, 80, text=str(rpm), font=("segoe ui semibold", 20))

    def change_gear():
        global gear, max_vel, min_vel, rpm_i, speed
        rpm_i = time.time()
        if speed >= max_vel:
            if gear < 4:
                gear += 1
            if gear == 2:
                max_vel = 45
                min_vel = 15
            if gear == 3:
                max_vel = 70
                min_vel = 45
            if gear == 4:
                max_vel = 100
                min_vel = 70

    def low_gear():
        global gear, max_vel, min_vel, gear_lowered, rpm_i
        gear_lowered = True
        rpm_i = time.time()
        if gear > 1:
            if gear == 4:
                max_vel = 70
                min_vel = 45
            if gear == 3:
                max_vel = 45
                min_vel = 15
            if gear == 2:
                max_vel = 15
                min_vel = 10
            gear -= 1

#   acelerar
    def acelerar():
        global speed, max_vel, gear, gear_lowered
        gear_lowered = False
        aumento = 1
        if gear == 2:
            aumento = 3
        if 3 <= gear <= 4:
            aumento = 5
        if speed < max_vel:
            speed = speed + aumento
        update_stats()

#   simulacion de desaceleracion
    def desacelera():
        global speed, max_vel, min_vel, gear_lowered
        if gear_lowered:
            if speed > min_vel:
                speed -= 1
            update_stats()

#   Frena el carro
    def frenar():
        global deteniendo, speed, gear, min_vel, max_vel
        deteniendo = time.time()
        fin = time.time()
        speed -= 1
        if fin - deteniendo >= 2:
            gear = 1
            speed = 10
            min_vel = 10
            max_vel = 15
#   Mueve competidores

    def mover_competidores(velocidad):
        global revasados_count, revasados
        pos1 = C_game.coords(C1)
        pos2 = C_game.coords(C2)
        C_game.move(C1, 0, velocidad)
        C_game.move(C2, 0, velocidad)
        print(pos1, pos2)
        if pos1[1] >= 500:
            if pos1[0] == 85:
                C_game.move(C1, random.randrange(130, 260, 130), -1100)
            if pos1[0] == 215:
                C_game.move(C1, random.randrange(-130, 130, 260), -700)
            if pos1[0] == 345:
                C_game.move(C1, random.randrange(-260, -130, 130), -850)
            revasados_count += 1
            revasados.set(revasados_count)

        if pos2[1] >= 500:
            if pos2[0] == 85:
                C_game.move(C2, random.randrange(130, 260, 130), -800)
            if pos2[0] == 215:
                C_game.move(C2, random.randrange(-130, 130, 260), -650)
            if pos2[0] == 345:
                C_game.move(C2, random.randrange(-260, -130, 130), -900)
            revasados_count += 1
            revasados.set(revasados_count)


#   Mueve referencias
    def move_refereces(speed):
        """
        mueve los elementos de la pantalla del juego de acuerdo a la velocidad definida
        :param speed:
        :return :
        """
        global recorrido, recorrido_dato
        pos = C_game.coords(left_reference)
        C_game.move(left_reference, 0, speed)
        C_game.move(right_reference, 0, speed)


        if pos[3] >= 540:
            C_game.move(right_reference, 0, -(550-110/6))
            C_game.move(left_reference, 0, -(550 - 110 / 6))
            recorrido_dato += 0.25
            recorrido.set(recorrido_dato)

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
    def ver_gana():
        global recorrido_dato
        if recorrido_dato == 7:
            recorrido_dato = 0
            gana()

    def ver_pierde():
        if (C_game.coords(C1)[1] >= 420 and C_game.coords(C1)[0] == C_game.coords(carro)[0]) or \
                (C_game.coords(C2)[1] >= 420 and C_game.coords(C2)[0] == C_game.coords(carro)[0]):
            pierde()
#   BOTONES IN-GAME
    juego.bind("<Right>", lambda event: change_gear())
    juego.bind("d", lambda event: derecha())
    juego.bind("D", lambda event: derecha())
    juego.bind("<Left>", lambda event: low_gear())
    juego.bind("a", lambda event: izquierda())
    juego.bind("A", lambda event: izquierda())
    juego.bind("<Return>", lambda event: acelerar())
    juego.bind("<Up>", lambda event: change_gear())
    juego.bind("<Down>", lambda event: low_gear())
    juego.bind("z", lambda event: frenar())
    juego.bind("Z", lambda event: frenar())
    #Botón de salir
    ttk.Button(C_main, text="SALIR", command=lambda: Main(juego)).place(x=1198, y=690)

    while True:
        contar_tiempo()
        move_refereces(speed)
        mover_competidores(speed-3)
        contar_tiempo()
        desacelera()
        make_chage()
        ver_gana()
        ver_pierde()
        juego.update()
        time.sleep(0.1)


# BOTONES DE INICIO
img_play = cargarImg("play.gif")
img_about = cargarImg("info.gif")
play = Button(C_main, image=img_play, command=lambda: Game())
play.place(x=465, y=310)


about = Button(C_main, image=img_about, command=lambda: About())
about.place(y=630, x=1190)

# Binds Enter key to Game() function

root.bind("<Return>", lambda event: Game())

# MAINLOOP
root.mainloop()
