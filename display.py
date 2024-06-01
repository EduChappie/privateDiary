from tkinter import *
from tkinter import ttk
import os

root = Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Write your message!")

#Texto de mensagem principal
label1 = Label(root, text="Deixe sua marca")
label1.place(width=600, height=60)

def sendMSG():
	v = art.get("1.0", END)
	print("Enviando mensagem")
	print(v)
	root.destroy()

#Botao de Envio de artigo
button1 = Button(root, text="Enviar", command=sendMSG)
button1.place(x=260, y=60, width=80, height=20)


art = Text(root)
art.place(x=50, y=90, width=500, height=250)
art.insert("1.0", """ -> Meu Titulo

	Escreva uma ideia ou pensamento seu, 
como por exemplo... o que voce esta afim de comer?

 - Ass. Eduardo
Obs. nao se preocupe em assinar ou com data
o sistema ja faz isso  =)""")

#Botao de Sair
button2 = Button(root, text="Cancelar", command=root.destroy)
button2.place(x=260, y=360, width=80, height=20)

root.mainloop()
