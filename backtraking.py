import sys
import time
  
def isSafe(board, row, col): 
    for i in range(col): 
        if board[row][i] == 1: 
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False
  
    for i, j in zip(range(row, N, 1), range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False
  
    return True
  
def solveNQUtil(board, col): 
    end_time = time.process_time() - start_time
    print("\nTempo Atual: %s" %(end_time))
    if col >= N: 
        return True

    for i in range(N): 
  
        if isSafe(board, i, col):            
            board[i][col] = 1            
            if solveNQUtil(board, col + 1) == True: 
                return True
            board[i][col] = 0
    return False

def solveNQ(): 
    board = [[0]*N for _ in range(N)]
  
    if solveNQUtil(board, 0) == False:
        arquivo = open('backtraking.txt','a')
        print("\n Solution does not exist\n")
        arquivo.write("\n Solution does not exist")
        arquivo.close() 
        return False
    return True
  
if __name__ == "__main__":
    for N in range(10, 12):
        Tempo_Total = 0
        arquivo = open('backtraking.txt','a')
        print("\n ******** NUMERO DE RAINHAS: %d ********\n" %(N))
        arquivo.write("\n ******** NUMERO DE RAINHAS: %d ********\n" %(N))
        arquivo.close()
        for i in range (1, 4):
            board = [[0]*N for _ in range(N)]
            start_time = time.process_time()
            solveNQ() 
            end_time = time.process_time()
            Tempo_Total += end_time - start_time
            arquivo = open('backtraking.txt','a')
            print("Execução %d:" %(i))
            arquivo.write("Execucao %d:\n" %(i))
            print("Tempo da execução %d: %s\n"%(i , end_time - start_time))
            arquivo.write("Tempo da execucao %d: %s\n"%(i , end_time - start_time ))
            arquivo.close()
        Tempo_Total = Tempo_Total / 3
        arquivo = open('backtraking.txt','a')
        print("\nMedia de tempo de execução: %s\n"%(Tempo_Total))
        arquivo.write("\nMedia de tempo de execucao %s\n"%(Tempo_Total))
        print("==============================================")
        arquivo.write("==============================================")
        arquivo.close()
    sys.exit()
