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
	# de vertices todos os vertices, sem repetição e em ordem crescente 	
	for i in range(len(lista)):
		for j in range(2):
			if lista[i][j] not in listaVertices:
				listaVertices.append(lista[i][j])
	listaVertices.sort()
	
	return listaVertices

def geraMI(grafo):
	lin = len(grafo.arestas)
	col = len(grafo.vertices)
	matriz = []
	for i in range(lin):
		linha = []
		for j in range(col):
			if str(j) in grafo.arestas[i][:2]:
				if str(j) == grafo.arestas[i][0]:
					linha.append(grafo.arestas[i][2])
				else:
					linha.append('-' + grafo.arestas[i][2])
			else:
				linha.append('0')
		matriz.append(linha)
	return matriz

def imprimirMI(matriz):
	linhas = len(matriz)
	colunas = len(matriz[0])
	for i in range(linhas):
		for j in range(colunas):
			print(matriz[i][j]," ",end = "")
		print()

#n5_dir_unwgt_comb0.txt
#n10_dir_wgt_comb3.txt
























