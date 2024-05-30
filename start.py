
import os

def menu():
	#botar codigo de sleep, o arquivo  nao ta sendo criado no tempo certo
	with open("/home/.myOwnJournal/config.edu", "r") as file:
		data = file.readlines()
		print(data)
		username = data[0].replace('nome ', '')
		username = username.replace(' \n', '')
		email = data[1].replace('email ', '')

	print("""
#################################
#	     Jornal		#
#################################""")
	print("- {} - horario e dia".format(username))
	print("- {}".format(email))

def createConfig(n, e):
	print("usuario criado")
	print("['nome', '{}']".format(n))
	print("['email', '{}']".format(e))
	conf = open("/home/.myOwnJournal/config.edu", "w")
	conf.write("nome {} \nemail {}".format(n, e))
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
	configUser()
