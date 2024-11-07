"""
1) Relacione as colunas de acordo com o tipo de variável

(5) "Casa"
(3) 2 + 0j
(4) True
(5) '123'
(2) 1.2345
(4) False
(5) '''2j'''
(3) 10 + 1j
(1) 2
(5) 'Programando Ideias'

2) Faça um programa que receba o nome de um aluno e quando ele tirou na prova de programalção.
   depois imprima em apenas uma linha o nome no modo title() e quanto a pessoa tirou na proca.
   Ex: Ana Carolina tirou 8.
"""

nome = input('Digite o seu nome do aluno: ')
nota = input('Digite a nota do aluno:  ')
print(f'{nome.title()} tirou {nota}')
