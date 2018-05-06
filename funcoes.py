#Função que verifica se o grafo é direcionado 
#ou não-direcionado por meio da leitura da primeira linha do arquivo
def direcionadoOuNao(arq):
	caminhoArquivo = "instances/Padrao_Txt/" + arq
	arquivo = open(caminhoArquivo,'r')
	direcao = arquivo.readline()
	direcao = direcao.rstrip()
	if direcao == 'DIRECTED':
		ehDirecionado = True
	else:
		ehDirecionado = False
	
	arquivo.close()
	return ehDirecionado

#Função que cria uma lista em que cada elemento dessa lista 
#é a ligação de um vértice
def listarLigacoes(arq):
	caminhoArquivo = "instances/Padrao_Txt/" + arq
	arquivo = open(caminhoArquivo,'r')
	lista = []
	#Para cada linha do arquivo cria uma lista com os vértices pertencentes
	#à aresta. Ao final  temos como retorno uma lista de listas 
	#Cada elemento da lista  final é um par(u,v) representando uma aresta 	
	for linha in arquivo:
		lista.append(linha.split())
	lista.pop(0)
	arquivo.close()
	return lista

#Função que cria uma lista em que cada elemento dessa lista 
#é um vértice
def listarVertices(arq):
	arq = "instances/Padrao_Txt/" + arq
	arquivo = open(arq,'r')
	lista = []
	for linha in arquivo:
		lista.append(linha.split())
	lista.pop(0)
	arquivo.close()
	listaVertices = []
	#Percorre cada aresta (par de vértices) da lista inserindo em uma lista
	# de vertices todos os vertices sem repetição e em ordem crescente 	
	for par in lista:
		for elemento in par:
			if elemento not in listaVertices:
				listaVertices.append(elemento)
	listaVertices.sort()
	
	return listaVertices
	
	
#n5_dir_unwgt_comb0.txt


