# IMPORTS
from model.Pessoa import Pessoa

# CLASSES
class PessoaDAO:
	# ATRIBUTOS
	conexao	= None
	cursor	= None

	
	# CONSTRUTOR
	def __init__(self, con, cur):
		self.conexao = con
		self.cursor = cur

	# LER A TABELA INTEIRA
	def getAll(self, orderBy = False):
		sql = "SELECT id, nome FROM pessoa"
		if orderBy == True:
			sql = sql + "ORDER BY nome ASC"
    		
		try:
      			self.cursor.execute(sql)
      			resultado = self.cursor.fetchall()

      			pessoas = []
      			for linha in resultado:
        			pessoa = Pessoa(linha[0], linha[1])
        			pessoas.append(pessoa)

      			return pessoas
		except Exception as e:
      			return e
 	
	
	# INSERIR NO BANCO
      	 #Função/método para inserir no banco.
	def save(self, pessoa):
		sql = "INSERT INTO pessoa (nome) VALUES (%s)"
		
		try:
			self.cursor.execute(sql, pessoa.nome)
			pessoa.id = self.cursor.lastrowid
			pessoa.commit()
			return pessoa
		except Exception as e:
			return e

        	