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
	



