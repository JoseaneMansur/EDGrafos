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
	for linha in arquivo:
		linha = linha.rstrip()
		lista = lista + [linha]
	lista.pop(0)
	arquivo.close()
	return lista

#n5_dir_unwgt_comb0.txt


