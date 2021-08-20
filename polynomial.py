import math
import random
import time
import sys

def inicializaTabuleiro(numeroRainhas):

	for i in range(0, numeroRainhas):
		rainhas.append(i)

	for count in range(0, numeroDiagonais):
		count1 = count
		if (count % 2 == 0):
			diagonal_posistiva[count]= 1
		else:
			diagonal_posistiva[count]= 0
		
		count2 = count
		if (count1 == ((numeroDiagonais) / 2)):
			count1 = math.ceil(count1)
			count2 = count1
			diagonal_negativa[count2]=  numeroRainhas
		else:
			diagonal_negativa[count2]=  0
	
	rainhaUm = random.randint(0,numeroRainhas-1)
	rainhaDois = random.randint(0,numeroRainhas-1)

	for i in range(0, numeroRainhas):
		Swap(rainhaUm, rainhaDois)		  

def Swap(Coluna01, Coluna02):

	linha01 = rainhas[Coluna01]
	linha02 = rainhas[Coluna02]

	'''********************* Primeira Rainha ******************************'''
	Diagonais_Pos_Aux = linha01 + Coluna01
	Diagonais_Neg_Aux = (Coluna01 - linha01) + (numeroRainhas - 1)
	diagonal_posistiva[Diagonais_Pos_Aux] = diagonal_posistiva[Diagonais_Pos_Aux] - 1
	diagonal_negativa[Diagonais_Neg_Aux] = diagonal_negativa[Diagonais_Neg_Aux] - 1

	Diagonais_Pos_Aux = linha02 + Coluna01
	Diagonais_Neg_Aux = ((Coluna01 - linha02) + (numeroRainhas - 1))
	diagonal_posistiva[Diagonais_Pos_Aux] = diagonal_posistiva[Diagonais_Pos_Aux] + 1
	diagonal_negativa[Diagonais_Neg_Aux] = diagonal_negativa[Diagonais_Neg_Aux] + 1

	'''******************** Segunda Rainha ********************************'''

	Diagonais_Pos_Aux = linha02 + Coluna02
	Diagonais_Neg_Aux = (Coluna02 - linha02) + (numeroRainhas - 1)
	diagonal_posistiva[Diagonais_Pos_Aux] = diagonal_posistiva[Diagonais_Pos_Aux] - 1
	diagonal_negativa[Diagonais_Neg_Aux] = diagonal_negativa[Diagonais_Neg_Aux] - 1

	Diagonais_Pos_Aux = linha01 + Coluna02
	Diagonais_Neg_Aux = (Coluna02 - linha01) + (numeroRainhas - 1)
	diagonal_posistiva[Diagonais_Pos_Aux] = diagonal_posistiva[Diagonais_Pos_Aux] + 1
	diagonal_negativa[Diagonais_Neg_Aux] = diagonal_negativa[Diagonais_Neg_Aux] + 1

	'''******************* Substitui rainhas ********************************'''

	rainhas[Coluna01] = linha02
	rainhas[Coluna02] = linha01

def Verifica_Ataques_Rainhas(Coluna):
	Ataques = False
	if (diagonal_posistiva[procura_diagonal_Pos(Coluna)] > 1):
		return True
	
	if (diagonal_negativa[procura_diagonal_Neg(Coluna)] > 1):
		return True
	
	return Ataques   

def procura_diagonal_Pos(Coluna):
	diagonal = -1
	diagonal = Coluna + rainhas[Coluna]
	return diagonal

def procura_diagonal_Neg(Coluna):
	diagonal = -1
	diagonal = (Coluna - rainhas[Coluna]) + (numeroRainhas - 1)
	return diagonal

def Verifica_ataques():
	ataques = 0

	for Diagonal_count in range(0, numeroDiagonais):
		if (diagonal_posistiva[Diagonal_count] > 1):

			ataques = ataques + diagonal_posistiva[Diagonal_count] - 1
		
		if (diagonal_negativa[Diagonal_count] > 1):
		
			ataques = ataques + diagonal_negativa[Diagonal_count] - 1			   

	return ataques


def test():
	for Diagonal_count in range(0, numeroDiagonais):
		if (diagonal_posistiva[Diagonal_count] > 1):	 
			return False	

		if (diagonal_negativa[Diagonal_count] > 1):
			return False	 
	
	return True


def Controlador(): 
	colisoes01 = 0 
	colisoes02 = 0
	rainhas_aux = [0,0]

	swap_perform = 1
	while (swap_perform != 0): 
		swap_perform = 0
		for coluna01 in range(0, numeroRainhas - 1):
			for coluna02 in range(coluna01 + 1, numeroRainhas):
				if ((Verifica_Ataques_Rainhas(coluna01) == True) or (Verifica_Ataques_Rainhas(coluna02) == True)):
					colisoes01 = Verifica_ataques()
					Swap(coluna01, coluna02)
					colisoes02 = Verifica_ataques()
					swap_perform = swap_perform + 1
					if (colisoes01 == 0): 
						swap_perform = 0
					if (colisoes01 < colisoes02): 
						Swap(coluna01, coluna02)
						swap_perform = swap_perform - 1
	
	#if (test()):
	#	return

def imprime():
	for i in range(0, numeroRainhas):
		for i1 in range(0, numeroRainhas):
			if (rainhas[i1] == i): 
				print(" " +str( i )+" ", end="")
			else: 
				print(" X ", end="")
				   
		print(" ")
	print(" ")

if __name__ == '__main__':
	for numeroRainhas in range(80000, 110000, 10000):
		Tempo_Total = 0
		rainhas = []
		numeroDiagonais = (numeroRainhas * 2) - 1
		diagonal_posistiva = [i for i in range(numeroDiagonais)]
		diagonal_negativa = [i for i in range(numeroDiagonais)]
		inicializaTabuleiro(numeroRainhas)
		arquivo = open('polynomial.txt','a')
		print("\n ******** NUMERO DE RAINHAS: %d ********\n" %(numeroRainhas))
		arquivo.write("\n ******** NUMERO DE RAINHAS: %d ********\n" %(numeroRainhas))
		arquivo.close()
		for i in range (1, 4):
			start_time = time.process_time()
			Controlador()
			end_time = time.process_time() - start_time
			Tempo_Total += end_time
			arquivo = open('polynomial.txt','a')
			print("Execução %d:" %(i))
			arquivo.write("Execucao %d:\n" %(i))
			print("Tempo da execução %d: %s\n"%(i , end_time))
			arquivo.write("Tempo da execucao %d: %s\n"%(i , end_time))
			arquivo.close()
		Tempo_Total = Tempo_Total / 3
		arquivo = open('polynomial.txt','a')
		print("\nMedia de tempo de execução: %s\n"%(Tempo_Total))
		arquivo.write("\nMedia de tempo de execucao %s\n"%(Tempo_Total))
		print("==============================================")
		arquivo.write("==============================================")
		arquivo.close()
	sys.exit()

