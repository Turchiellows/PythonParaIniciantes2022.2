###############################################################################
# IMPORTS
###############################################################################
from model.Pessoa 	import Pessoa
from database.Database 	import Database
from dao.PessoaDAO 	import PessoaDAO





###############################################################################
# FUNÇÕES
###############################################################################
# FUNÇÃO DE CABEÇALHO
def header(message):
	print('#' * (len(message) + 50))
	print(message.upper())
	print('#' *  (len(message) + 50))
	print()





###############################################################################
# ORIENTAÇÃO A OBJETO
###############################################################################
# CABEÇALHO
header('Aula 05')

# OBJETO PESSOA
ps1 = Pessoa(1, 'Elias')
print(ps1)

# OBJETO EM BANCO DE DADOS
db 		= Database()
pessoaDAO 	= PessoaDAO(db.conexao, db.cursor)
pessoas		= pessoaDAO.getAll(True)
for p in pessoas:
	print(p)

novo = Pessoa(0, 'teste')
novo = pessoaDAO.save(novo)

pessoas		= pessoaDAO.getAll(True)
for p in pessoas:
	print(p)