print('#' * 80)
print('Início da aula 3'.upper())
print('#' * 80)
print()

# CONFIGURAÇÕES PARA EXIBIÇÃO
char1 = '='
char2 = '-'
char3 = '+'










# CRIANDO FUNÇÕES
# CABEÇALHO
def header(message, ch):
	print(ch * len(message))
	print(message.upper())
	print(ch * len(message))

# RODAPÉ
def footer(ch):
	print(ch * 80)
	print()

# IMPOSTO
def tax_calculator(val, tax):
	imposto = val * (tax / 100)
	return imposto









# CONTADOR MANUAL
title = 'contador em loop com while'
header(title, char1)

contador = 1
print(contador)
contador = contador + 1
print(contador)

footer(char3)










# CONTADOR EM LOOP USANDO WHILE
title = 'contador em loop com while'
header(title, char1)

contador	= 0
fim		= 5
while (contador <= fim):
	print(contador)
	contador = contador + 1

footer(char3)










# USANDO LISTAS E LOOP
title = 'trabalhando com for e listas'
header(title, char1)

frutas = [
 "Banana", "Abacate", "Melancia", "Melão", "Caqui", "Laranja", "Manga"
]
print(f'Quantidade de frutas : {len(frutas)}')
print(f'Tudo junto           : {frutas}')
print(f'Somente a terceira   : {frutas[2]}')
frutas.append("Ameixa")
print(f'Nova lista de frutas : {frutas}')

# WHILE
print(f'\nusando while'.upper())
x = 0
while (x < len(frutas)):
	print(f'{x} -> {frutas[x]}')
	x = x + 1

# FOR
print(f'\nusando for\n'.upper())
for k, v in enumerate(frutas):
	print(f'{k} -> {v}')

footer(char3)










# CALCULANDO IMPOSTO
title='calculando imposto'
header(title, char1)

pr = [ 220.99, 54.38, 36.99, 6814.50, 9446566.99, 1.99]
ta = 5.25 # %
for i in pr:
	result = tax_calculator(i, ta)
	print(f'O imposto {ta}% de {i} é: {result:.2f}')

footer(char3)
