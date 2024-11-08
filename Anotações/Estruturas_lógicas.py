"""
Estruturas lógicas

and (e): True apenas se todas as condições forem True

or (ou): True quando pelo menos uma condição for True

is (é): Comparação entre valores, similar ao ==

nort (não): Inversão do valor Booleano (True -> False, False -> True)

#and
#Exemplo 1
sensor = 58 #range de segurança do sensor: 60 a 75

if sensor >= 60 and sensor <= 75:
    print('Tudo OK!')
else:
    print('Corre!')

#Exemplo 2
agua = True
comida = True

if agua and comida:
    print('Cahorro feliz!')
else:
    print('Cachorro triste!')

# Or
# Exemplo 1
pizza = True
lasanha = False
if pizza or lasanha:
    print('Preciso comer mais salada')
else:
    print('Estou com fome')

# Exemplo 2
num = 17

if num % 2 == 0 or num <= 10:
    print('É par ou menor que 10')
else:
    print('É impar e maior que 10')

# Is
login = False
#print(login is True) #login é True? R: NÃO (False)
#print(login is False) #login é False? R: SIM (True)

if login is True:
    print('Logado')
else:
    print('Deslogado')
"""

# not
login = False

if not login: # não False: True
    print('Deslogado')
else:
    print('Logado')
