#Função que verifica se o grafo é direcionado 
#ou não-direcionado por meio da leitura da primeira linha do arquivo
def direcionadoOuNao(arq):
	arq = "instances/Padrao_Txt/" + arq
	manipulador = open(arq,'r')
	direcao = manipulador.readline()
	direcao = direcao.rstrip()
	if direcao == 'DIRECTED':
		ehDirecionado = True
	else:
		ehDirecionado = False
	
	manipulador.close()
	return ehDirecionado

#Função que cria uma lista em que cada elemento dessa lista 
#é a ligação de um vértice
def listarLigacoes(arq):
	arq = "instances/Padrao_Txt/" + arq
	manipulador = open(arq,'r')
	lista = []
	for linha in manipulador:
		linha = linha.rstrip()
		lista = lista + [linha]
	lista.pop(0)
	manipulador.close()
	return lista
	
#n5_dir_unwgt_comb0.txt


