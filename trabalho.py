from funcoes import *
from classes import *

nomeArquivo = input("Digite o nome do arquivo: ")
#resultado = direcionadoOuNao(nomeArquivo)
lista = listarLigacoes(nomeArquivo)
print(lista)


listaA = listarLigacoes(nomeArquivo)
listaV = listarVertices(nomeArquivo)
grafo = Grafo(listaV,listaA)
print('Vertices: ', grafo.vertices)
print('Arestas: ', grafo.arestas)
