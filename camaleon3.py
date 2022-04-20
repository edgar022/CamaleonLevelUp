import tkinter
import random
from tkinter import font

ventana=tkinter.Tk()
ventana.geometry("200x200")
ventana.title("camaleon")
colors=["green","black","pink","blue","gray","purple"]


def changeColor():

    randomcolor = random.choice(colors)
    ventana.config(background=randomcolor)
    pk=tkinter.Label(ventana,text=randomcolor,font="cambria 25",width=15,height=2,fg="white",bg="gray")
    pk.place(x= 496,y=300)

background=tkinter.Label(ventana, text="background color:", font="cambria 25", width=30, height=4, fg="white", bg="purple")
background.place(x=370, y=100)
boton=tkinter.Button(ventana, text="cambia", width=10, height=5, command=changeColor)
boton.place(x=600,y=400)

ventana.mainloop()