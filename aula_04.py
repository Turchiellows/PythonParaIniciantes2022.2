###############################################################################
# IMPORTS
###############################################################################
import sqlite3





###############################################################################
# CONFIGURAÇÂO
###############################################################################
db_file = "dc_universe.db"





###############################################################################
# FUNÇÕES
###############################################################################
# FUNÇÃO DE CABEÇALHO
def header(message):
	print('#' * (len(message) + 50))
	print(message.upper())
	print('#' *  (len(message) + 50))
	print()


# EXECUTA QUERY
def db_query_execute(query):
	# CRIANDO A CONEXÃO
	connection = sqlite3.connect(db_file)

	# CRIANDO O CURSOR
	cursor = connection.cursor()

	# EXECUTANDOs
	cursor.execute(query)
	connection.commit()
	result = cursor.fetchall()
	connection.close()
	return result


# MOSTRA NA TELA
def db_show_result(arr_data):
	print(f'-' * 80)
	for x in arr_data:
		print(f'{x}')
	print(f'-' * 80)


# LER UMA TABELA INTEIRA
def db_get_all(table):
	sql	= f'select * from {table}'
	result	= db_query_execute(sql)
	db_show_result(result)


# OBTER O ÚLTIMO ID
def db_get_last_id(table, column):
	sql	= f'select max({column}) + 1 from {table}'
	proximo = db_query_execute(sql)
	return proximo[0][0]


# INSERE UM REGISTRO NA TABELA
def db_insert_person(data):
	# COLETANDO O ÚLTIMO ID
	id = db_get_last_id('pessoas', 'pessoa_id')

	# MONTANDO A QUERY E INSERINDO NO BANCO
	sql = f"insert into pessoas(pessoa_id, nome, nome_civil, tipo) values({id}, \'{data['nome']}\', \'{data['nome_civil']}\', \'{data['tipo']}\')"
	result = db_query_execute(sql)
	return id


# INSERIR PESSOA NA TABELA QUE VINCULA PESSOAS E GRUPOS
def db_insere_pessoa_grupo(id_p, id_g):
	sql 	= f"insert into pessoas_grupos (pessoa_id, grupo_id) values ({id_p}, {id_g})"
	result 	= db_query_execute(sql)
	return result


# APAGAR REGISTROS COM BASE NO ID	
def db_delete_by_id(table, column, id):
	sql	= f'delete from {table} where {column} = {id}'
	result	= db_query_execute(sql)
	return result


# LER TUDO DA TABELA PESSOAS_GRUPO DE FORMA AMIGÁVEL
def db_get_all_pessoas_grupo():
	sql	= f'SELECT pessoas.pessoa_id, pessoas.nome as pessoa, grupos.grupo_id, grupos.nome as grupo FROM pessoas INNER JOIN pessoas_grupos ON pessoas.pessoa_id = pessoas_grupos.pessoa_id INNER JOIN grupos ON pessoas_grupos.grupo_id = grupos.grupo_id'
	result	= db_query_execute(sql)
	db_show_result(result)





###############################################################################
# INÍCIO
###############################################################################
# CABEÇALHO
header("Início da aula 4")





###############################################################################
# TESTES UNITÁRIOS
###############################################################################
# LISTANDO TUDO DA TABELA
# db_get_all('pessoas')





# INSERINDO DADOS NA TABELA E MOSTRANDO O RESULTADO
# id 	= db_get_last_id('pessoas', 'pessoa_id')
# sql	= f"insert into pessoas(pessoa_id, nome, nome_civil, tipo) values({id}, 'Elias Bernabe Turchiello', 'Alguma coisa', 'Herói(na)')"
# result	= db_query_execute(sql)

# db_get_all('pessoas')





# APAGANDO O REGISTRO INSERIDO
# id 	= db_get_last_id('pessoas', 'pessoa_id')
# # db_delete_by_id('pessoas', 'pessoa_id', '14')
# db_delete_by_id('pessoas', 'pessoa_id', (id -1))

# db_get_all('pessoas')





###############################################################################
# TESTES DINÂMICOS
###############################################################################
# MANIPULANDO DADOS DINAMICAMENTE
continuar=True
while continuar:
	# COLETA
	data 			= {}
	data['nome']		= str(input('Digite o nome: '))
	data['nome_civil']	= str(input('Digite o nome civil: '))
	option	= str(input('''Esolha o tipo:\n1 - Herói ou heroína\n2 - Vilão ou vilã\nSua escolha: '''))
	if option == '1':
		data['tipo'] = 'Herói(na)'
	else:
		data['tipo'] = 'Vilã(o)'

	# INSERE A PESSOA
	last_id = db_insert_person(data)


	# LISTAR OS GRUPOS EXISTENTES PARA SELECIONAR UM
	db_get_all('grupos')
	id_grupo = int(input('Informe o número ID do grupo ao qual deseja inserir a pessoa recem cadastrada: '))


	# INSERIR A NOVA PESSOA NO GRUPO SELECIONADO
	db_insere_pessoa_grupo(last_id, id_grupo)
	

	# EXIBINDO O BANCO DE DADOS
	db_get_all('pessoas')
	db_get_all('grupos')
	db_get_all('pessoas_grupos')
	db_get_all_pessoas_grupo()

	
	# DESCIDE SE PARA OU NÃO
	stop = str(input('Deseja parar? [N/s]'))
	if stop.upper() == 'S' or stop.upper() == 'SIM':
		continuar = False
