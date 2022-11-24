# IMPORTS
import sqlite3

# CLASSE
class Database:
	# ATRIBUTOS
	conexao	= None
	cursor	= None


	# MÉTODOS
	def __init___(self):
		self.conexao	= sqlite3.connect('database/imdb.db')
		self.cursor	= self.connexao.cursor()

	def _del__(self):
		self.conexao.commit()
	