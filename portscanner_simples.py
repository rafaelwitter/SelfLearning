import socket

portas = [21, 23, 80, 443, 8080]
host = str(input("Digite o endereco desejado: "))
for porta in portas:
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(1)
    codigo = cliente.connect_ex((host, porta))
    if codigo == 0:
       print(porta, "OPEN")
    else:
       print(porta, "closed")

