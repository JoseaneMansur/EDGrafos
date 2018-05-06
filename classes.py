#Classe que representa um grafo lido do arquivo
class Grafo(object):
	def __init__(self, vertices,arestas, direcionado):
		self.vertices = vertices
		self.arestas = arestas
		self.direcionado = direcionado

