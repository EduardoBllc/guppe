"""
Estruturas de repetição
For

C ou Java:
for(i = 0; i < limitador; i++){
    //Execução do loop
}

Python:
for i in interável:
    //Execução do loop

Utiliza-se loops para iterar sobre sequências de valores ou sobre valores iteráveis

Exemplos de iteráveis:
- String
nome = "Eduardo Salvagni Ballico"

- Lista
lista = [1, 3, 5, 7, 9]

- Range
numeros = range(1,10)
"""

nome = "Eduardo Salvagni Ballico"

lista = [1, 3, 5, 7, 9]

numeros = range(1, 10)
"""
range(valor_inicial, valor_final)
OBS: O valor final não é incluído
"""

for letra in nome:
    print(letra)

for item in lista:
    print(item)

for numero in numeros:
    print(numero)
