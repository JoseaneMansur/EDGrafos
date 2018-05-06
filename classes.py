class Grafo(object):
	def __init__(self, vertices,arestas, direcionado):
		self.vertices = vertices
		self.arestas = arestas
		self.direcionado = direcionado
class Matriz_Adj(object):
	pass

class MatrizInc(object):
	def __init__(self,grafo):
		self.matriz = []
		lin = len(grafo.arestas)
		col = len(grafo.vertices)
		for i in range(lin):
			linha = []			
			for j in range(col):
				linha.append('0')
		self.matriz.append(linha)		
		for i in range(len(grafo.arestas)):			
			for aresta in grafo.arestas:
				self.matriz[i][int(aresta[0])] = '-' + aresta[2]
				self.matriz[i][int(aresta[1])] = aresta[2]				
				if(grafo.direcionado == True):
					self.matriz[int(aresta[1])][int(aresta[0])] = aresta[2]
