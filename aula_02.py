# CABEÇALHO
print('#' * 80)
print('Início da aula 2'.upper())
print('#' * 80)
print()









# INPUT E IF
nome = str(input('Digite seu nome: '))
idade = int(input('Qual dua idade? '))
genero = int(input('Gênero:\n1 - Masculino\n2 - Feminino\nComo você se identifica? '))
idade2 = idade * 2

print()
print('-' * 80)
print(f'Seu nome é: {nome}, sua idade é {idade} e o dobro dela é {idade2}')
print()

if idade >= 18:
	print(f'Você é maior de idade, não deveria depender de seus pais')
	
	if genero == 1 and idade <= 19:
		print(f'Você está na faixa etária para servir o exército')
else:
	print(f'Você ainda é dependente de seus pais')
print()
print('-' * 80)
print()

aluno = str(input('Qual seu nome: '))
nota = float(input('Qual sua nota: '))
if nota == 10:
	print(f'Muito bom!!')
elif nota >= 7:
	print(f'Você passou! ')
else:
	print(f'Tente melhorar')

print()
print('-' * 80)
print()









# WHILE
x = 1
while x <= 10:
	print(f'{x}')
	x += 1


print()
print('-' * 80)
print()