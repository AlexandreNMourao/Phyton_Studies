"""
Input e Output

Output - print(): Apresenta dados para o usuário

Input - input(): Recebe dados do usuário

# Obs: Os dados recebidos são do tipo String.

# Print sem pular linha
print('tomate')
print('tomate')
print('tomate')

print('tomate', end=' ')
print('tomate', end=' ')
print('tomate', end=' ')

#print('Digite uma cor: ')
#cor = input()

# Versões 2.x
#print('Você escolheu a cor %s' % cor)

# Versões 3.x até 3.7
#print('Você escolher a cor {}'.format(cor))

# Versões a partir da 3.7
#print(f'Você escolheu a cor {cor}')

cor = input('Digite uma cor: ')

num = input('Digite um número: ')

print(f'Você escolheu a cor {cor} e o número {num}')
"""

#Realizar operações nas saídas (print)

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
soma = num1 + num2
print(f'A soma dos valores é {soma}')

#Obs: Casting - conversão de um tipo de dado para outro