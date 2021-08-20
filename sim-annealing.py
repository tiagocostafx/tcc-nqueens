import random
from math import exp
import time
import sys
from copy import deepcopy

def threat_calculate(n):
    if n < 2:
        return 0
    if n == 2:
        return 1
    return (n - 1) * n / 2


def create_board(n):
    chess_board = {}
    temp = list(range(n))
    random.shuffle(temp) 
    column = 0

    while len(temp) > 0:
        row = random.choice(temp)
        chess_board[column] = row
        temp.remove(row)
        column += 1
    del temp
    return chess_board


def cost(chess_board):
    threat = 0
    m_chessboard = {}
    a_chessboard = {}

    for column in chess_board:
        temp_m = column - chess_board[column]
        temp_a = column + chess_board[column]
        if temp_m not in m_chessboard:
            m_chessboard[temp_m] = 1
        else:
            m_chessboard[temp_m] += 1
        if temp_a not in a_chessboard:
            a_chessboard[temp_a] = 1
        else:
            a_chessboard[temp_a] += 1

    for i in m_chessboard:
        threat += threat_calculate(m_chessboard[i])
    del m_chessboard

    for i in a_chessboard:
        threat += threat_calculate(a_chessboard[i])
    del a_chessboard

    return threat


def simulated_annealing(N, temperature):
    '''Simulated Annealing'''
    solution_found = False
    answer = create_board(N)
    cost_answer = cost(answer)
    t = temperature
    sch = 0.99

    while t > 0:
        t *= sch
        successor = deepcopy(answer)
        while True:
            index_1 = random.randrange(0, N - 1)
            index_2 = random.randrange(0, N - 1)
            if index_1 != index_2:
                break
        successor[index_1], successor[index_2] = successor[index_2], \
            successor[index_1]  
        delta = cost(successor) - cost_answer
        if delta < 0 or random.uniform(0, 1) < exp(-delta / t):
            answer = deepcopy(successor)
            cost_answer = cost(answer)
        if cost_answer == 0:
            solution_found = True
            break
    if solution_found is False:
        print("Failed")

def main():
    for N in range(11, 12):
        Tempo_Total = 0
        arquivo = open('sim-annealing.txt','a')
        print("\n ******** NUMERO DE RAINHAS: %d ********\n" %(N))
        arquivo.write("\n ******** NUMERO DE RAINHAS: %d ********\n" %(N))
        arquivo.close()
        for i in range (1, 4):
            TEMPERATURA = 4000
            start_time = time.process_time()
            simulated_annealing(N, TEMPERATURA)
            end_time = time.process_time() - start_time
            Tempo_Total += end_time
            arquivo = open('sim_annealing-2.txt','a')
            print("Execução %d:" %(i))
            arquivo.write("Execucao %d:\n" %(i))
            print("Tempo da execução %d: %s\n"%(i , end_time))
            arquivo.write("Tempo da execucao %d: %s\n"%(i , end_time))
            arquivo.close()
        Tempo_Total = Tempo_Total / 3
        arquivo = open('sim_annealing-2.txt','a')
        print("\nMedia de tempo de execução: %s\n"%(Tempo_Total))
        arquivo.write("\nMedia de tempo de execucao %s\n"%(Tempo_Total))
        print("==============================================")
        arquivo.write("==============================================")
        arquivo.close()
    sys.exit()

if __name__ == "__main__":
    main()