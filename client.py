# !/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import print_function
import socket
import sys
import pickle

with open('ports.txt', 'r') as file:
    content = file.readlines()
    HOST = content[1]  # Endereco IP do Servidor
    PORT = int(content[0])  # Porta que o Servidor está


# Criando a conexão
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
destino = (HOST, PORT)
tcp.connect(destino)

print('\nDigite suas mensagens')
print('Para sair use CTRL+X\n')

# Recebendo a mensagem do usuário final pelo teclado
mensagem = input()

# Enviando a mensagem para o Servidor TCP através da conexão
while mensagem != '\x18':
    tcp.send(mensagem.encode())
    data = tcp.recv(1024)
    if not data:
        break
    if mensagem[0] == 'G':
        print(pickle.loads(data))
    else:
        print(data.decode())

    mensagem = input()

# Fechando o Socket
tcp.close()
