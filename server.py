#!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import print_function
import socket
import os
import sys

import rank

import routines  # Recursos adversos
import pickle  # Necessário para formatar a lista

__author__ = "Leandro de Gonzaga Peres"

# Garantindo o utf-8 no windows
if os.name == "nt":
    os.system("@echo off > nul")
    os.system("chcp 65001 > nul")
    os.system("set PYTHONIOENCODING=utf-8")
    os.system("title CellAs server")
    os.system("cls")
else:
    sys.stdout.write("\x1b]2;CellAs server\x07")
    sys.stdout.write('clear')

print(u'Leandro, Senac Goiânia - 2018/2')
# Informações sobre o ecossistema
routines.sysinfo()

# Endereco IP do Servidor. No caso, um loopback ip, ou o endereço da rede local.
HOST = '127.0.0.1'
PORT = 0  # Porta de comunicação do servidor 65535 máximo, 0 mínimo. Caso 0, será qualquer porta aberta

# Iniciando o socket e definindo o makefile
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
self = (HOST, PORT)  # Agrupando as informações

# Aplicando o endereço IP e a porta no Socket
# tcp.bind(self)
try:
    tcp.bind((HOST, PORT))
except (socket.error, msg):
    print('Falha no bind. Error Code: ' + str(msg[0]) + '\nMessage ' + msg[1])
    sys.exit()

# Garante ao server aceitar conexões
tcp.listen(1)

print('\nServidor TCP iniciado em', HOST, 'na porta', tcp.getsockname()[1])

# A seguir, torna-se viável o jogo reconhecer a porta e o host
with open(routines.path_join('ports.txt'), 'w') as file:
    file.write("{1}:{0}".format(tcp.getsockname()[1], tcp.getsockname()[0]))

session = rank.Rank()  # Inicializa o rank

try:
    while True:
        # Aceitando uma nova conexão
        conexao, cliente = tcp.accept()
        print('\n\n[+]', cliente)

        while True:
            # Recebendo as mensagens através da conexão
            mensagem = conexao.recv(1024)

            # Conexão encerrada
            if not mensagem:
                break
            else:
                # Bytes para str.utf-8
                mensagem = mensagem.decode()
                print('\n\n['+mensagem+']', cliente)

            if mensagem[0] == "G":  # Recuperar o rank
                # Se for uma solicitação de toda a lista
                if mensagem[-1] == "G" or mensagem[-1] == "0":
                    conexao.send(pickle.dumps(session.__list__))
                elif mensagem[1:].isdigit():  # Seleciona
                    try:
                        new = []
                        for i in range(int(mensagem[1:])):
                            new.append(session.__list__[i])

                        conexao.send(pickle.dumps(new))
                    except (IndexError):
                        # Erro. provavelmente porque a lista não possui tal tamanho
                        conexao.send(pickle.dumps(new))

                elif mensagem[1:] == "I":
                    routines.sysinfo()

            elif mensagem[0] == "+":  # Introduzir
                if len(mensagem) > 0:
                    isOkay = bytes(session.introduce(mensagem[1:]))
                    conexao.send(isOkay)
                else:
                    conexao.send(bytes(0))

            elif mensagem[0] == "-":  # remover
                if len(mensagem) > 0:
                    isOkay = bytes(session.remove(mensagem[1:]))
                    conexao.send(isOkay)
                else:
                    conexao.send(bytes(0))

        # Exibindo a mensagem de finalização da conexão
        print('\n\n[-]', cliente)

        # Fechando a conexão com o Socket
        conexao.close()
except (KeyboardInterrupt, SystemExit):
    os.remove(routines.path_join("ports.txt"))
    conexao.close()
    sys.exit(0)
