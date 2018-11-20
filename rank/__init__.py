# !/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import print_function
from routines import *
import csv

__author__ = 'Leandro Peres'
__all__ = ['Rank']


class Rank(object):
    r"""
    Classe para carregar e dispor, se requisitado, o rank.
    Além de realizar os cálculos para reorganizar o 'data.csv'
    """

    def __init__(self):
        # Abre o arquivo do rank no python3
        with open(path_join('rank/data.csv'), newline='', encoding='utf-8') as element:
            self.__list__ = []  # Inicializa a lista do rank
            self.maxID = 0  # Inicializa o maior ID

            for _ in csv.DictReader(
                    element):  # Recuperar o arquivo csv como dicionário
                # Aplicar cada linha em uma lista
                self.__list__.append(dict(_))
        self.organize()

    def organize(self):
        r"""
        Organiza o Rank em ordem cerscente
        """

        for i in range(len(self.__list__)):  # Loop central do organizador
            for j in range(i + 1, len(self.__list__)
                           ):  # Loop que descarta objetos já 'analisados'

                if int(self.__list__[i]['score']) < int(self.__list__[
                        j]['score']):  # Caso o antecessor(i) seja menor
                    self.__list__[i], self.__list__[j] = self.__list__[
                        j], self.__list__[i]  # Altera as posições adequadamente

            if self.maxID < int(
                    self.__list__[i]['id']):  # Caso o maxID seja menor que o analisado
                self.maxID = int(self.__list__[i]['id'])

    def introduce(self, row):
        r"""
        Insere na lista um dado elemento

        Params:
            :str: row ex.: 'Spinoza 13000 900'
        """
        try:
            row = row.split(",") if row.find(',') != -1 else row.split()  # Separando a informação fornecida pelo jogo
            if len(row) < 3:
                return False  # Previne falta de dados

            # Definindo as etiquetas das colunas
            base = [
                'id',
                'name',
                'score',
                'time']

            row.insert(0, self.maxID + 1)  # Insere o ID a ser escrito

            # Converte em dict após 'zipar' as duas listas
            new = dict(zip(base, row))

            self.__list__.append(new)  # Adiciona na lista de dicts
            self.organize()
            self.save()

            return True
        except:
            return False

    def remove(self, id):
        r"""
        Remove da lista o elemento que for de igual identidade na coluna 'id'

        Params:
            :int: id
        """
        try:
            for i in self.__list__:  # Para cada elemento
                if int(i['id']) == int(id):  # Se o elemento for o desejado
                    self.__list__.remove(i)  # Remova-o
                    break

            self.organize()
            self.save()
            return True
        except:
            return False

    def save(self):
        r"""
        Salva o self.__init__, do rank, no arquivo data.csv
        """

        keys = self.__list__[0].keys()  # Captando as chaves id, score, ...
        with open('rank/data.csv', 'w') as output_file:  # Enquanto um arquivo para escrever
            dict_writer = csv.DictWriter(
                output_file, keys)  # Transforma o dict em csv
            dict_writer.writeheader()  # Escreve o nome das colunas
            dict_writer.writerows(self.__list__)  # Escreve os itens da coluna
