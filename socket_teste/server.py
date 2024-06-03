import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


s.bind(('', 8081))
print("No aguarda da conexão...")


while True:
    conn, ip = s.recvfrom(2048)
    res = conn.decode().upper()

    s.sendto(res.encode(), ip)
    print("mensage convertida: " + res)
    break
