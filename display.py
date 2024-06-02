from tkinter import *
from tkinter import ttk
from datetime import datetime
from datetime import date
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
	print("escrevendo...")

	# pegando dados da config
	user = open("/home/.myOwnJournal/config.edu", "r")
	p = user.readlines()
	# - email do usuario (take)
	em = p[1].replace('email', '')
	user.close()

	#pegando as horas
	now = datetime.now()

	#pegando a quantidade
	with open("/home/.myOwnJournal/artigos/many.edu", "r") as quanto:
		qtd = quanto.read()
		qtd = int(qtd)

		# adicionando valor no arquivo
		artigo_atual = open("/home/.myOwnJournal/artigos/art{}.txt".format(qtd+1), "w")
		artigo_atual.write("""{}
{} - {}:{}:{}
--------------------
{}
--------------------""".format(em, date.today(), now.hour, now.minute, now.second, v))
		artigo_atual.close()

	# atualizando o arquivo de quantidade
	ytq = open("/home/.myOwnJournal/artigos/many.edu", "w")
	ytq.write(str(qtd+1))
	ytq.close()

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
