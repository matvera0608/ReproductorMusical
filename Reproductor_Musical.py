from tkinter import Button, Label, Tk,filedialog, ttk, Frame, PhotoImage
from webbrowser import BackgroundBrowser
from click import style
import pygame
import random
import mutagen

pygame.mixer.init()
pygame.mixer.init(frequency=94000)
cancion_actual = ''
direccion = ''

#Lista de funciones para abrir archivo, iniciar
def abrir_archivo():
    global direccion, pos, n,cancion_actual
    pos = 0
    n = 0
    direccion = filedialog.askopenfilenames(initialdir='/', title= 'Escoger la canción(es)',
                                            filetype=(('mp3 files', '*.mp3*'), ('All files', '*.*')))
    
    n = len(direccion)
    cancion_actual = direccion[pos]
    
    nombre_cancion = cancion_actual.split('/')
    nombre_cancion = nombre_cancion[-1]
    
lista = []
for i in range(50, 200, 1):
    lista.append(i)
    
def iniciar_reproduccion():
    global cancion_actual, direccion, pos, n, actualizar
    barra1['value'] = random.choice(lista)
    barra2['value'] = random.choice(lista)
    barra3['value'] = random.choice(lista)
    barra4['value'] = random.choice(lista)
    barra5['value'] = random.choice(lista)
    barra6['value'] = random.choice(lista)
    barra7['value'] = random.choice(lista)
    barra8['value'] = random.choice(lista)
    barra9['value'] = random.choice(lista)
    barra10['value'] = random.choice(lista)
    barra11['value'] = random.choice(lista)
    barra12['value'] = random.choice(lista)
    barra13['value'] = random.choice(lista)
    barra14['value'] = random.choice(lista)
    barra15['value'] = random.choice(lista)
    barra16['value'] = random.choice(lista)
    barra17['value'] = random.choice(lista)
    barra18['value'] = random.choice(lista)
    barra19['value'] = random.choice(lista)
    barra20['value'] = random.choice(lista)

    cancion_actual = direccion[pos]
    nombre_cancion = cancion_actual.split('/')
    nombre_cancion = nombre_cancion[-1]
    nombre['text'] = nombre_cancion
    
    time = pygame.mixer.music.get_pos()
    x = int(int(time)*0.001)
    tiempo['value'] = x
    
    y = float(int(volumen.get())*0.01)
    pygame.mixer.music.set_volume(y)
    nivel['text']= int(y*100)
    
    audio = mutagen.File(cancion_actual)
    log = audio.info.length
    minutos, segundos = divmod(log, 60)
    
    minutos, segundos = int(minutos), int(segundos)
    tt = minutos*60 + segundos
    tiempo['maximum']= tt
    texto['text']= str(minutos) + ":" + str(segundos)
    
    actualizar = ventana.after(100, iniciar_reproduccion)
    
    if x == tt:
        ventana.after_cancel(actualizar)
        texto['text']= "00:00"
        detener_efecto()
        
        if pos != n:
            pos = pos + 1
            ventana.after(100, iniciar_reproduccion)
            pygame.mixer.music.play()
        if pos == n:
            pos = 0
            
def iniciar():
    global cancion_actual
    pygame.mixer.music.load(cancion_actual)
    pygame.mixer.music.play()
    iniciar_reproduccion()
    
def retroceder():
    global pos,n
    
    if pos > 0:
        pos -= 1
    else:
        pos = 0
    cantidad['text'] = str(pos)+'/'+ str(n)
    
def adelantar():
    global pos, n
    
    if pos == n-1:
        pos = 0
    else:
        pos += 1
    cantidad['text'] = str(pos)+'/'+str(n)
    
def detener_efecto():
    barra1['value'] = 50
    barra2['value'] = 60
    barra3['value'] = 70
    barra4['value'] = 80
    barra5['value'] = 90
    barra6['value'] = 100
    barra7['value'] = 90
    barra8['value'] = 80
    barra9['value'] = 70
    barra10['value'] = 60
    barra11['value'] = 60
    barra12['value'] = 70
    barra13['value'] = 80
    barra14['value'] = 90
    barra15['value'] = 100
    barra16['value'] = 90
    barra17['value'] = 80
    barra18['value'] = 70
    barra19['value'] = 60
    barra20['value'] = 50
    
def stop():
    global actualizar
    pygame.mixer.music.stop()
    ventana.after_cancel(actualizar)
    detener_efecto()
    
    
def pausa():
    global actualizar
    pygame.mixer.music.pause()
    ventana.after(100, iniciar_reproduccion)
    detener_efecto()


def continuar():
    pygame.mixer.music.unpause()
    ventana.after(100, iniciar_reproduccion)

def pantallaPrincipal():
    global ventana, barra1, barra2, barra3, barra4, barra5, barra6, barra7, barra8, barra9, barra10, barra11, barra12, barra13, barra14, barra15, barra16, barra17, barra18, barra19, barra20
    global cancion_actual, direccion, pos, n, tiempo, texto, nombre, cantidad, nivel, volumen
    global actualizar, imagen1, imagen2, imagen3, imagen4, imagen5, imagen6, imagen7
    
    ventana =Tk()
    ventana.title('Player made by Ramiro Mateo Vera')
    ventana.iconbitmap(icono)
    ventana.config(bg='black')
    ventana.resizable(0,0)

    estilo = ttk.Style()
    estilo.theme_use('clam')
    estilo.configure("Vertical.TProgressbar", foreground= 'red', background= 'red', troughcolor='black',
                    bordercolor='black', lightcolor='red', darkcolor='red')

    frame1 = Frame(ventana, bg='black', width=700, height=50)
    frame1.grid(column=0, row=0, sticky='nsew')
    frame2 = Frame(ventana, bg='black', width=700, height=50)
    frame2.grid(column=0, row=1, sticky='nsew')

    #Creé las barras para la música
    barra1 = ttk.Progressbar(frame1, orient= 'vertical', length=300, maximum=300, style="Vertical.TProgressbar")
    barra1.grid(column=0, row=0, padx = 1)
    barra2 = ttk.Progressbar(frame1, orient= 'vertical', length=300, maximum=300, style="Vertical.TProgressbar")
    barra2.grid(column=1, row=0, padx = 1)
    barra3 = ttk.Progressbar(frame1, orient= 'vertical', length=300, maximum=300, style="Vertical.TProgressbar")
    barra3.grid(column=2, row=0, padx = 1)
    barra4 = ttk.Progressbar(frame1, orient= 'vertical', length=300, maximum=300, style="Vertical.TProgressbar")
    barra4.grid(column=3, row=0, padx = 1)
    barra5 = ttk.Progressbar(frame1, orient= 'vertical', length=300, maximum=300, style="Vertical.TProgressbar")
    barra5.grid(column=4, row=0, padx = 1)
    barra6 = ttk.Progressbar(frame1, orient= 'vertical', length=300, maximum=300, style="Vertical.TProgressbar")
    barra6.grid(column=5, row=0, padx = 1)
    barra7 = ttk.Progressbar(frame1, orient= 'vertical', length=300, maximum=300, style="Vertical.TProgressbar")
    barra7.grid(column=6, row=0, padx = 1)
    barra8 = ttk.Progressbar(frame1, orient= 'vertical', length=300, maximum=300, style="Vertical.TProgressbar")
    barra8.grid(column=7, row=0, padx = 1)
    barra9 = ttk.Progressbar(frame1, orient= 'vertical', length=300, maximum=300, style="Vertical.TProgressbar")
    barra9.grid(column=8, row=0, padx = 1)
    barra10 = ttk.Progressbar(frame1, orient= 'vertical', length=300, maximum=300, style="Vertical.TProgressbar")
    barra10.grid(column=9, row=0, padx = 1)
    barra11 = ttk.Progressbar(frame1, orient= 'vertical', length=300, maximum=300, style="Vertical.TProgressbar")
    barra11.grid(column=10, row=0, padx = 1)
    barra12 = ttk.Progressbar(frame1, orient= 'vertical', length=300, maximum=300, style="Vertical.TProgressbar")
    barra12.grid(column=11, row=0, padx = 1)
    barra13 = ttk.Progressbar(frame1, orient= 'vertical', length=300, maximum=300, style="Vertical.TProgressbar")
    barra13.grid(column=12, row=0, padx = 1)
    barra14 = ttk.Progressbar(frame1, orient= 'vertical', length=300, maximum=300, style="Vertical.TProgressbar")
    barra14.grid(column=13, row=0, padx = 1)
    barra15 = ttk.Progressbar(frame1, orient= 'vertical', length=300, maximum=300, style="Vertical.TProgressbar")
    barra15.grid(column=14, row=0, padx = 1)
    barra16 = ttk.Progressbar(frame1, orient= 'vertical', length=300, maximum=300, style="Vertical.TProgressbar")
    barra16.grid(column=15, row=0, padx = 1)
    barra17 = ttk.Progressbar(frame1, orient= 'vertical', length=300, maximum=300, style="Vertical.TProgressbar")
    barra17.grid(column=16, row=0, padx = 1)
    barra18 = ttk.Progressbar(frame1, orient= 'vertical', length=300, maximum=300, style="Vertical.TProgressbar")
    barra18.grid(column=17, row=0, padx = 1)
    barra19 = ttk.Progressbar(frame1, orient= 'vertical', length=300, maximum=300, style="Vertical.TProgressbar")
    barra19.grid(column=18, row=0, padx = 1)
    barra20 = ttk.Progressbar(frame1, orient= 'vertical', length=300, maximum=300, style="Vertical.TProgressbar")
    barra20.grid(column=19, row=0, padx = 1)

    estilo1 = ttk.Style()
    estilo1.theme_use('clam')
    estilo1.configure("Horizontal.TProgressbar", foreground='red', background='#FF4000', troughcolor='#00FFFF',
                    bordercolor='#00FFFF', lightcolor='#00FFFF', darkcolor='#FF4000')

    tiempo = ttk.Progressbar(frame2, orient= 'horizontal', length= 550, mode='determinate', style="Horizontal.TProgressbar")
    tiempo.grid(row=0, columnspan=8, padx=5)
    texto = Label(frame2, bg='black', fg='green2', width=5)
    texto.grid(row=0, column=8)


    nombre = Label(frame2, bg='black', fg='red', width=55)
    nombre.grid(column=0, row=1, columnspan=8, padx=5)
    cantidad = Label(frame2, bg='black', fg='green2')
    cantidad.grid(column=8, row=1)


    #Imágenes para los iconos de los botones
    imagen1 = PhotoImage(file='openfile.png')
    imagen2 = PhotoImage(file='play.png')
    imagen3 = PhotoImage(file='pause.png')
    imagen4 = PhotoImage(file='loop.png')
    imagen5 = PhotoImage(file='stop.png')
    imagen6 = PhotoImage(file='previous.png')
    imagen7 = PhotoImage(file='next.png')

    #Creé las listas de botones
    boton1 = Button(frame2, image= imagen1, bg='black', command= abrir_archivo)
    boton1.grid(column=0, row=2, pady=10)
    boton2 = Button(frame2, image= imagen2, bg='black', command= iniciar)
    boton2.grid(column=1, row=2, pady=10)
    boton3 = Button(frame2, image= imagen3, bg='black', command= pausa)
    boton3.grid(column=2, row=2, pady=10)
    boton4 = Button(frame2, image= imagen4, bg='black', command= continuar)
    boton4.grid(column=3, row=2, pady=10)
    boton5 = Button(frame2, image= imagen5, bg='black', command= stop)
    boton5.grid(column=4, row=2, pady=10)
    boton6 = Button(frame2, image= imagen6, bg='black', command= retroceder)
    boton6.grid(column=5, row=2, pady=10)
    boton7 = Button(frame2, image= imagen7, bg='black', command= adelantar)
    boton7.grid(column=6, row=2, pady=10)

    #Subo o bajo el volumen
    volumen = ttk.Scale(frame2, to = 100, from_ = 0, orient='horizontal', length=100, style='Horizontal.TScale')
    volumen.grid(column=7, row=2)

    style = ttk.Style()
    style.configure("Horizontal.TScale", bordercolor= 'blue', troughcolor='black', background= 'green2',
                    foreground='green2', lightcolor='blue', darkcolor='green2')

    nivel = Label(frame2, bg='black', fg='green2', width=3)
    nivel.grid(column=10, row=2)
    return ventana

icono = PhotoImage(file='iconomusica.ico')

pantallaPrincipal().mainloop()

pygame.mixer.quit()