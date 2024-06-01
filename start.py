import os
from time import sleep
from datetime import date

def loadConfig():
	#carrega as informacoes dos nomes
	with open("/home/.myOwnJournal/config.edu", "r") as file:
		data = file.readlines()
		username = data[0].replace('nome ', '')
		username = username.replace(' \n', '')
		email = data[1].replace('email ', '')

	return username, email

# Funcao para ler todos os artigos
def readAll(u):
	#identifica a quantidade de artigos e bota num arquivo
	os.system("ls -l /home/.myOwnJournal/artigos/art* | wc -l > /home/.myOwnJournal/artigos/many.edu")
	with open("/home/.myOwnJournal/artigos/many.edu", "r") as howMany:
		i = int(howMany.read())
		os.system("clear")
		if i==0:
			return

		for x in range(i): # indo em cada arquivo existente
			with open("/home/.myOwnJournal/artigos/art{}.txt".format(x+1), "r") as file:
				d = file.read()
				print("--- {} --------------".format(x+1))
				print(d) # mostrando os dados escritos no arquivo
		y = input("Aperte [Enter] para voltar...")
		return


# Funcao para escrever os artigos
def writeFile():
	print(".\nescreva um artigo...")
	os.system("sudo python3 display.py")


def menu():
	os.system("clear")
	username, email = loadConfig()
	print("""
#################################
#	     Diary		#
#################################""")
	print("Usuario: {} - Data: {}".format(username, date.today()))
	print(".")

	while True:
		print("""
#################################
#    [1] Ler todos os artigo    #
#    [2] Escrever um artigo     #
#    [3] Sair                   #
#################################""")
		res =  str(input("R="))

		if res=="1":
			readAll(username)

		elif res=="2":
			writeFile()

		elif res=="3":
			#sair
			print("Tchau {}".format(username))
			exit()

		else:
			#nao reconhecido
			print("Comando nao reconhecido\nTente de novo\n.")
			os.system("clear")
			menu()

def createConfig(n, e):
	print(".\nusuario criado\n.")
	conf = open("/home/.myOwnJournal/config.edu", "w")
	conf.write("nome {} \nemail {}".format(n, e))
	conf.close()

	many = open("/home/.myOwnJournal/artigos/many.edu", "w")
	many.write("0")
	many.close()

	menu()


def configUser():
        nome_atual = input("Qual o seu nome? = ")
        email_atual = input("Qual o seu email? = ")
        print(".")
        print("nome: [{}]\nemail: [{}]".format(nome_atual, email_atual))
        res = str(input("tudo certo? (y/n)"))
        if res=="y" or res=="yes":
                createConfig(nome_atual, email_atual)
        else:
                configUser()

## comeco do codigo
i = os.path.isdir("/home/.myOwnJournal")
if i==True: # se existir pasta
	c = os.path.isfile("/home/.myOwnJournal/config.edu")
	if c==True: # e se existir config.edu
		menu()
	else: # e se nao existir, crie
		configUser()
else: # se nao existir, crie
	os.mkdir("/home/.myOwnJournal")
	os.mkdir("/home/.myOwnJournal/artigos")
	configUser()
