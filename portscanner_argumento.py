import socket
import sys

portas = [21, 23, 80, 443, 8080]
host = sys.argv
for porta in portas:
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(1)
    codigo = cliente.connect_ex((host[1], porta))
    if codigo == 0:
       print(porta, "OPEN")
    else:
       print(porta, "closed")
