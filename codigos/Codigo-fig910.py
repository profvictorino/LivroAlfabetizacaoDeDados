"""
Implemente um algoritmo utilizando laço condicional com teste no início
que leia a idade de várias pessoas e no final apresente a média das idades.
O critério de parada será a digitação de uma idade menor ou igual a zero.
"""

cont = 0
total = 0

idade = int(input('Informe uma idade: '))

while (idade > 0):
    total = total + idade
    cont = cont + 1
    idade = int(input('Informe uma idade: '))

media = total/cont
print('A média de idade é: ', media)
    

