class Pessoa:
	# ATRIBUTOS
	id = None
	nome = None

	# CONSTRUTOR
	def __init__(self, id, nome):
		self.id 	= id
		self.nome 	= nome


	# MOSTRADOR DE ATRIBUTOS
	def __str__(self):
		return f'{self.id} - {self.nome}'