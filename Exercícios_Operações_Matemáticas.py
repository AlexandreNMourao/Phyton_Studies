"""
1 - Realizar a média das notas de 4 alunos.

2- Converter uma temperatura em graus Celcius para fairenheit e para kelvin.
Dados: F = C * 1.8 +32, K = C + 273.15


nota1 = float(input('Digite a nota do primeiro aluno: '))
nota2 = float(input('Digite a nota do segundo aluno: '))
nota3 = float(input('Digite a nota do terceiro aluno: '))
nota4 = float(input('Digite a nota do quarto aluno: '))
media = (nota1 + nota2 + nota3 + nota4) / 4
print(f'A média das notas é {media}')
"""

tempC = float(input('Digite a temperatura em °C: '))
tempF = tempC * 1.8 + 32
tempK = tempC + 273.15
print(f'A temperatura de {tempC}°C vai para {tempF}°F e {tempK}°K')
