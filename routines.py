# !/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import print_function
import os
import psutil
import logging
import platform

APP_DIR = os.path.dirname(os.path.abspath(__file__))
__version__ = '0.3.2'

def path_join(name):
    r"""
    Relativo à informação acerca do diretório em execução

    Args:
        name (str): O nome do arquivo.

    Returns:
        str: Retorna o caminho absoluto do arquivo.
    """
    return os.path.join(APP_DIR, name)


def sysinfo(printa=True):
    r"""
    Relativo à informação acerca do ecosistema em execução

    args:
        printa: bool: Se vai retornar no terminal ou pelo socket

    prints:
        str: Kernel name / Kernel version
        str: Machine name / CPU cores

        str: CPU usage in %
        str: RAM usage in %
    """
    # Comando padrão para informações acerca do contexto operativo
    UNAME = {0:'os', 1:'name', 2:'version'}
    
    # Selecionando apenas as 3 primeiras informações
    for i in range(0, 3):
        UNAME[i] = platform.uname()[i]

    # Segregando para obter a informação necessária
    UNAME[2] = UNAME[2].split('-')[0] if UNAME[2] != "Linux" else UNAME[2]

    # Requisitando o número de núcleos e a porcentagem de uso da unidade lógica
    # T = Total
    # % = Uso em porcentagem
    CPU = {'T': psutil.cpu_count(), '%': psutil.cpu_percent()}

    # Requisitando o tamanho total, em bytes, e a porcentagem do uso da memória
    # GiB = (B / 1024) / (2^20)
    RAM = {'T': (psutil.virtual_memory()[0] / 1024) / (2 ** 20), '%': psutil.virtual_memory()[2]}

    # Mostragem
    print(u"\nCellAs {0}\nPID {1}\n\n".format(__version__,  os.getpid()))
    print(u"Executando no {0} de versão {1}.".format(UNAME[0], UNAME[2]))
    print(u"{0} possuiu {1} núcleos lógicos.".format(UNAME[1], CPU['T']))
    print(u"Uso da CPU: {0}%".format(CPU['%']))
    print(u"Uso da RAM: {0}% de {1:.0f} GiB".format(RAM['%'], RAM['T']))
    print(u"Diretório: {0}\n".format(APP_DIR))