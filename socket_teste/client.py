import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

c.connect(("192.168.1.42", 2121))

while True:
    #pegando mensagem inicial e mostrando
    inicialtxt = c.recv(1024).decode()
    print(inicialtxt)
    print(' ')
    
    # pegando resposta e mandando resposta
    res = input(" = ")
    c.send(res.encode())

    if res=="2":
        print("especifique o artigo, exemplo (art1.txt)")
        art = str(input(" = ")).encode()
        c.send(art) # enviando arquivo especificado

        # esperar arquivo chegar
        file = c.recv(2048)
        # escrever no arquivo
        print("pegou o arquivo: " + file.decode())
        break

    if res=="3":
        allfile = c.recv(1000000)
        print("tudo recebido")
        print("isso vai ser estranho implementar, provavelmente vou tirar")
        break

    if res=="4":
        exit()
    
    # pegando resposta do servidor
    data = c.recv(1024).decode()
    print(data)

    
