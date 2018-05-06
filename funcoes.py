#Função que verifica se o grafo é direcionado 
#ou não-direcionado por meio da leitura da primeira linha do arquivo
def ehDirecionado(arq):
	caminhoArquivo = "instances/Padrao_Txt/" + arq
	arquivo = open(caminhoArquivo,'r')
	direcao = arquivo.readline()
	direcao = direcao.rstrip()
	arquivo.close()
	if direcao == 'DIRECTED':
		return True
	else:
		return False

#Função que verifica se o grafo é ponderado ou não
def ehPonderado(arq):
	caminhoArquivo = "instances/Padrao_Txt/" + arq
	arquivo = open(caminhoArquivo,'r')
	arquivo.readline()
	segundaLinha = arquivo.readline().split()
	arquivo.close()
	if(len(segundaLinha) > 2):
		return True
	else:
		return False

#Função que cria uma lista em que cada elemento dessa lista 
#é a ligação de um vértice
def listarArestas(arq):
	caminhoArquivo = "instances/Padrao_Txt/" + arq
	arquivo = open(caminhoArquivo,'r')
	lista = []
	#Para cada linha do arquivo cria uma lista com os vértices pertencentes
	#à aresta. Ao final  temos como retorno uma lista de listas 
	#Cada elemento da lista final possui 3 valores(u, v, p) em que
	#u e v são vértices e p representa o peso da aresta.
	if(ehPonderado(arq)): 	
		for linha in arquivo:
			lista.append(linha.split())
	else:
		for linha in arquivo:
			linha += str(1)		
			lista.append(linha.split())
	lista.pop(0)
	arquivo.close()
	return lista

#Função que cria uma lista em que cada elemento dessa lista 
#é um vértice
def listarVertices(arq):
	lista = listarArestas(arq)
	listaVertices = []
	#Percorre cada aresta (par de vértices) da lista inserindo em uma lista
	# de vertices todos os vertices sem repetição e em ordem crescente 	
	for par in lista:
		for elemento in par:
			if elemento not in listaVertices:
				listaVertices.append(elemento)
	listaVertices.sort()
	
	return listaVertices

def qntVertices(arq):
	return len(listarVertices(arq))

def criarMA(arq):
	caminhoArquivo = "instances/Padrao_Txt/" + arq
	arquivo = open(caminhoArquivo,'r')
	
	
	
	
#n5_dir_unwgt_comb0.txt
#n10_dir_wgt_comb3.txt
























