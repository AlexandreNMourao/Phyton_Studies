"""
Estruturas condicionais

if(se), elif(senão se), else(senão)

#Testar altura para brinquedo do parque
altura = float(input('Digite sua altura: '))
if altura < 1.6:
    print('Você não pode ir nesse brinquedo')
else:
    print('Você pode ir no brinquedo')

#Consultar média final para aprovação
nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
nota3 = float(input('Digite a sua terceira nota: '))
media = (nota1 + nota2 + nota3) / 3
print(f'Sua média foi {media}')
if media >= 6:
    print('Parabéns, você está aprovado')
elif media >=5 <6:
    print('Você está de recuperação')
else:
    print('Você está de recuperação')

# Determinar se um número é par ou ímpar
num = int(input('Digite um número: '))
if num % 2 == 0:
    print(f'{num} é par')
else:
    print(f'{num} é ímpar')

# Utilizando outros tipos de dados

# Strings

pais = input('Digite um país que você deseja visitar: ')
if pais == 'Noruega':
    print('Ah não, muito frio!')
elif pais == 'China':
    print('Ah não, muito longe!')
elif pais == 'Austrália':
    print('Ah não, muito canguru!')
else:
    print('Vamos!')

# Boolean

login = False
senha = 'Caneta1'

key = input('Digite sua senha: ')

if key == senha:
    login = True
else:
    print('Senha incorreta')

if login == True:
    print('Bem-vindo admin!')
else:
    print('Tente novamente!')

"""
from tarfile import TruncatedHeaderError

# Cuidado com as variáveis locais e globais

login = False # Variável Global
senha = 'Caneta1'
key = 'Caneta1'

if key == senha:
    login = True # Variável Local
else:
    print('Senha incorreta')

#if login == True:
if login:
    print('Bem-vindo admin!')
else:
    print('Tente novamente!')


"""
# Lista de operadores

> - maior
< - menor
>= - maior ou igual
<= - menor ou igual
== - igual
!= - diferente
% - resto da divisão
"""