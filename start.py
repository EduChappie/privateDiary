import os
from time import sleep
from datetime import date

def loadConfig():
	#dia = "{}/{}/{}".format(day, mes, ano)
	with open("/home/.myOwnJournal/config.edu", "r") as file:
		data = file.readlines()
		username = data[0].replace('nome ', '')
		username = username.replace(' \n', '')
		email = data[1].replace('email ', '')

	return username, email

def menu():
	username, email = loadConfig()
	print("""
#################################
#	     Jornal		#
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
			#readAll()
			print(".\nmostra todos os artigos")

		elif res=="2":
			#writeFile()
			print(".\nescreva um artigo")

		elif res=="3":
			#sair
			print("Tchau {}".format(username))
			exit()

		else:
			#nao reconhecido
			print("Comando nao reconhecido\nTente de novo\n.")
def createConfig(n, e):
	print(".\nusuario criado\n.")
	conf = open("/home/.myOwnJournal/config.edu", "w")
	conf.write("nome {} \nemail {}".format(n, e))
	conf.close()
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
