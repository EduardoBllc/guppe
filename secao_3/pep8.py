"""
PEP8 - Python Enhancement Proposals

São propostas de aprimoramento para a linguagem Python

The Zen of Python - import this

A ideia da PEP8 é que possamos escrever códigos Python de forma Pythônica.

[1] - Utilize Camel Case para nomes de classes;

class Calculadora:
    pass

class CalculadoraCientifica:
    pass

[2] - Utilize nomes em minúsculo separados por underline para funções ou variáveis

def soma():
    pass

def soma_dois():
    pass

numero = 4

numero_impar = 3

[3] - Utilizar 4 espaços para indentação! (NÃO use tab)

if 'a' in 'banana':
    print('tem')

[4] - linhas em branco
- Separar funções e definições de classe com duas linhas em branco
- Métodos dentro de uma classe devem ser separados com uma única linha em branco

[5] - Imports
- Imports devem sempre serem feitos em linhas separadas

Import Errado

import sys, os

Import Certo

import sys
import os

Não há problemas em utilizar:

from types import StringType, ListType

Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from types import(
    StringType
    ListType
    SetType
    OutroType
)

Imports devem colocados no topo do arquivo, logo depois de quaisquer comentários ou docstrings
e antes de constantes ou variáveis globais

[6] - Espaços em expressões
"""

# Não faça:

funcao( algo [ 1 ], { outro: 2 } )

# Faça:

funcao(algo[1], {outro: 2})

# Não faça:

funcao (1)

# Faça:

funcao(1)

# Não faça:












