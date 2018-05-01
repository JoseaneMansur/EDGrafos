
def direcionadoOuNao(arq):
	arquivo = arq
	arquivo = "instances/Padrao_Txt/" + arquivo
	print(arquivo)
	manipulador = open(arquivo,'r')
	direcao = manipulador.readline()
	direcao = direcao.rstrip()
	if direcao == 'DIRECTED':
		ehDirecionado = True
	else:
		ehDirecionado = False
		
	print(ehDirecionado)
	manipulador.close()



