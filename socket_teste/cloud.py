import socket
import os

while True:
    print("""
#########################################
#     Bem-vindo ao meu Cloud Service    #
# Para transferencia de dados entre PCs #
#########################################""")
    print("""   [1] Enviar
   [2] Receber
   [3] Receber e desligar PC
   [4] Sair
-----------------------------------------""")
    ans = str(input(" = "))
    
    if ans=="1": # enviar arquivos
        os.system("py .\client.py")
        p = input("\nAperte [Enter] para continuar...")
        os.system("cls")
    
    elif ans=="2" or ans=="3": # receber arquivos
        os.system("py .\server.py")

        if ans=="3":
            print("desligando PC")
            exit()
        
        exit()
    
    elif ans=="4": # desligar esse sistema
        exit()

    else:
        os.system("cls")
        print("err: comando não reconhecido.")