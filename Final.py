from tkinter import *

main = Tk()

main.title('Refuerzo educativo')

main.geometry('600x400')

main.resizable(0,0)

#main.iconbitmap('')

main.config(bg = 'Grey22')


def limpiar_ventana(main):
    for widget in main.winfo_children():
        widget.destroy()



def crear_ventana_Main():
    limpiar_ventana(main)

    bienvenida = Label(main, text = 'Eliger que tema quieres practicar!')
    bienvenida.config(bg = 'Grey22', width = 30, font = ('Helvetica', 15), fg = 'white')
    bienvenida.pack(side = 'top', pady = 20)

    frame_botones = Frame(main, bg = 'Grey22')
    frame_botones.pack(pady = 150)

    boton1 = Button(frame_botones, text="Matematicas", command = crear_ventana_Matematicas)
    boton1.grid(row = 0, column = 0, padx = 10) 

    boton2 = Button(frame_botones, text="Lengua", command = crear_ventana_Lengua)
    boton2.grid(row = 0, column = 1, padx = 10)

    boton3 = Button(frame_botones, text="Ingles", command = crear_ventana_Ingles)
    boton3.grid(row = 0, column = 2, padx = 10)

    boton4 = Button(frame_botones, text="Ciencias", command = crear_ventana_Ciencias)
    boton4.grid(row = 0, column = 3, padx = 10)

    boton5 = Button(frame_botones, text="Deportes", command = crear_ventana_Deportes)
    boton5.grid(row = 0, column = 4, padx = 10)

    main.mainloop()



def crear_ventana_Matematicas():
    limpiar_ventana(main)

    bienvenida = Label(main, text = 'Bienvenido al juego de matematicas!')
    bienvenida.config(bg = 'Grey22', width = 30, font = ('Helvetica', 15), fg = 'white')
    bienvenida.pack(side = 'top', pady = 20)

    retroceder = Button(main, text="<", command = crear_ventana_Main)
    retroceder.place(relx=0.02, y=360)


    

def crear_ventana_Lengua():
    limpiar_ventana(main)
    
    bienvenida = Label(main, text = 'Bienvenido al juego de Lengua!')
    bienvenida.config(bg = 'Grey22', width = 30, font = ('Helvetica', 15), fg = 'white')
    bienvenida.pack(side = 'top', pady = 20)

    retroceder = Button(main, text="<", command = crear_ventana_Main)
    retroceder.place(relx=0.02, y=360)


    

def crear_ventana_Ingles():
    limpiar_ventana(main)

    bienvenida = Label(main, text = 'Bienvenido al juego de Ingles!')
    bienvenida.config(bg = 'Grey22', width = 30, font = ('Helvetica', 15), fg = 'white')
    bienvenida.pack(side = 'top', pady = 20)

    retroceder = Button(main, text="<", command = crear_ventana_Main)
    retroceder.place(relx=0.02, y=360)
    

    

def crear_ventana_Ciencias():
    limpiar_ventana(main)

    bienvenida = Label(main, text = 'Bienvenido al juego de Ciencias!')
    bienvenida.config(bg = 'Grey22', width = 30, font = ('Helvetica', 15), fg = 'white')
    bienvenida.pack(side = 'top', pady = 20)

    retroceder = Button(main, text="<", command = crear_ventana_Main)
    retroceder.place(relx=0.02, y=360)

    

def crear_ventana_Deportes():
    limpiar_ventana(main)

    bienvenida = Label(main, text = 'Bienvenido al juego de Deportes!')
    bienvenida.config(bg = 'Grey22', width = 30, font = ('Helvetica', 15), fg = 'white')
    bienvenida.pack(side = 'top', pady = 20)

    retroceder = Button(main, text="<", command = crear_ventana_Main)
    retroceder.place(relx=0.02, y=360)

    


crear_ventana_Main()