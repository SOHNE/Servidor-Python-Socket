# Servidor Python Socket
Algum servidor desenvolvido para o jogo *CellAs (?)*.



[![Python Version](https://img.shields.io/badge/Python-3.7.1-green.svg?style=flat-square)](https://www.python.org/) [![Licença](https://img.shields.io/badge/Licença-GPLv3-blue.svg?style=flat-square)](https://www.gnu.org/licenses/gpl-3.0.pt-br.html)

___

#### Autor
###### Leandro de Gonzaga Peres

## Requisitos
Como contido em *requeriments.txt*
```pip install psutil```

## Conexão
A conexão é dada por uma porta aleatória e disponível, descoberto pelo arquivo *ports.txt*

## Comunicação Jogo~Server
A disposição do server é dada por caracteres simples em uma esquemática de comando.
Assim, espera-se a seguinte lista de *bytes-like*:
```
CellAs send 'G' to Server
             Requisita uma lista do rank.
             O número inteiro é o tamanho da lista de retorno.
             Para seleção de três linhas: 'G3'
             0 é padrão, para completo.
Server responds rank.__list__[:] to CellAs
                Lista atualizada do banco de dados contidos em rank/data.csv
                {'id': '3', 'name': 'Socrate', 'score': '13650', 'time': '900'}
                {'id': '9', 'name': 'Plato', 'score': '9564', 'time': '1200'}
                {'id': '5', 'name': 'Theaetetus', 'score': '40000', 'time': '-5'}




CellAs send '+Plato 500 0.0' to Server
            Modo de nova entrada
Server responds 'Modo de inserção' to Cellas
                 O estado é trocado para adição de dados.
                 Após o primeiro caractere, a entrada deve ser como a do exemplo.
                 Separados por um espaço e respectivamente: nome, pontuação e tempo.
                 Salvamento em disco e cálculo de posição competitiva automática.
Server responds 1 to CellAs
                Caso obtenha êxito. Se não, 0




CellAs send '-5' to Server
            Modo de nova entrada
Server responds 'Modo de insersão' to Cellas
                 O estado é trocado para remoção de dados.
                 Após o primeiro caractere, espara-se um número representando o id
                 Salvamento em disco e cálculo de posição competitiva automática.
Server responds 1 to CellAs
                Caso obtenha êxito. Se não, 0
```
___
[![readme version](https://img.shields.io/badge/%2F~.-lightgrey.svg?style=flat-square&colorA=808080&colorB=808080)![readme version](https://img.shields.io/badge/14%2F11%2F18--lightgrey.svg?style=flat-square&colorA=000000&colorB=ffffff)](https://works.sohne.com.br/taoj)

