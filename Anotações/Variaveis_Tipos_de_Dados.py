"""
Variáveis e Tipos de Dados
"""
"""
O que são variáveis?
 - São um modo de rotular ou nomear todos os dados pertencentes ao seu programa.
O que são Dados?
 - São todas as informações que serão utilizadas ao longo do seu código. Podendo ser
   números, palavras, frases, textos, entre outros.
   
Existem 2 tipos de variáveis:
1) Variavel Global: São variáveis que podem ser manipuladas ao longo de todo o código.
2) Variavel Local: São variaveis que podem ser manipuladas apenas em uma determinada parte
                   do programa.

Como declarar variáveis?
nome = dado

É necessário seguir algumas regras para nomear suas variáveis:
a) Em nome compostos devemos separar por underline ou letras maiúsculas.
Ex: 
Modo Certo (Pythonico): 
idadeJoao = 17
idade_joao = 17
IDADE_JOAO = 17
Modo Errado:
idadejoao = 17

b) Variaveis não devem possuir nenhum tipo de caracter especial (%, acentos, ç, ...)
Ex:
Modo Certo:
fracao = 100
Modo Errado:
fração = 100

c) Variaveis não devem possuir números em seu nome
Ex:
Modo Errado:
123 = 17
Modo Certo:
a123 = 17

Tipos de Dados:
a) Inteiros: Número que não possui casas decimais.
Ex:
idadeJoao = 17
print(tupe(idadeJoao)) # Para utilizar a função type faça: type(nome da variavel)

b) Flutuantes (float): Números que possuem casas decimais.
 - Utiliza-se ponto para separar os números, NÃO VÍGURLA.
 - Não utiliza espaços em volta do ponto. 
Ex:
precoBanana = 5.59
print(type(precoBanana))

c) Complexo:
 - Se um dado possuir a letra j é um número complexo, lembrando que precisa ter um número junto a ele.
Ex:
num_complexo = 2 - 2j
print(type(num_complexo))

d) Booleana:
 - O valor 1 representa True (Verdadeiro), enquando o valor 0 representa False (Falso).
Ex:
var_bool = True
print(type(var_bool))

e) String:
 - Todos os dados que estão entre aspas simples, aspas duplas ou aspas simples triplas.
 - Podem conter números e letras dentro dela.
 - Para inventer o conteúdo presente na string basta adicionar [::-1]
Ex:
var_string = 'Tom Cruise'
print(type(var_string))
var_string = "Tom Cruise"
print(type(var_string))
var_string = '''Tom Cruise'''
print(type(var_string))

var_string = 'Tom Cruise'
print(var_string[::-1])

"""

var_string = 'Tom Cruise'
print(var_string[4:10]) # Estou pegando a posição 4(c) até a posição 9(e)
