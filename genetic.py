# -*- coding: utf-8 -*-
import time
import random
import sys

# Função de custo
# Retorna o número de ataques
def custo(cromossomo):
    return sum([1 for i in range(Bord_Size) for j in range(i+1, Bord_Size) if abs(j-i) == abs(cromossomo[j] - cromossomo[i])])


# função de seleção
# seleção por torneio
def selecao_parental():
    tmp = (list(), Bord_Size)
    for _ in range(PopulationSize // 5):
        ch = random.choice(Populacao)
        if ch[-1] < tmp[1]:
            tmp = (ch, ch[-1])
    return tmp[0]


# Função de cruzamento
def crossover(parent1, parent2):
    children = list()
    for _ in range(random.randint(1, max_offspring)):
        child = [-1]*(Bord_Size + 1)
        p, q = random.randint(1, Bord_Size//2 - 1), random.randint(Bord_Size//2 + 1, Bord_Size - 2)
        child[p: q+1] = parent1[p: q+1]
        for i in range(p, q+1):
            if parent2[i] not in child:
                t = i
                while p <= t <= q:
                    t = parent2.index(parent1[t])
                child[t] = parent2[i]
        for j in range(Bord_Size):
            if child[j] == -1:
                child[j] = parent2[j]
        child[-1] = custo(child)
        children.append(child)
        parent1, parent2 = parent2, parent1
    return children


# Função de mutação
def mutacao(cromossomo):
    p, q = random.randint(0, Bord_Size - 1), random.randint(0, Bord_Size - 1)
    cromossomo[p], cromossomo[q] = cromossomo[q], cromossomo[p]
    cromossomo[-1] = custo(cromossomo)


if __name__ == "__main__":
    for Bord_Size in range(10, 1000):
        Tempo_Total = 0
        arquivo = open('genetic.txt','a')
        print("\n ******** NUMERO DE RAINHAS: %d ********\n" %(Bord_Size))
        arquivo.write("\n ******** NUMERO DE RAINHAS: %d ********\n" %(Bord_Size))
        arquivo.close()

        for i in range (1, 4):
            PopulationSize = 2 * Bord_Size              # Número máximo de indivíduos em uma população
            Populacao = list()                         # População
            max_children = PopulationSize//3            # Número máximo de filhos
            max_offspring = 2                           # Número máximo de descendentes por cruzamento
            probabilidadeDeCrossover = 0.5                  # Probabilidade de cruzamento 
            probabilidadedeMutacao = 0.95                  # Probabilidade de mutatação

            cost_list = list()
            iteration_count = 0
            start_time = time.process_time()

            # inicialização PopulationSize e cromossomo
            for _ in range(PopulationSize):
                cromossomo = list(range(1, Bord_Size + 1))
                random.shuffle(cromossomo)
                cromossomo.append(custo(cromossomo))
                Populacao.append(cromossomo)

            # ordenação da população com chave de custo
            Populacao.sort(key=lambda q: q[-1])
            cost_list.append(Populacao[0][-1])

            # Início do algorítmo
            while Populacao[4][-1]:
                random.shuffle(Populacao)
                # recombina parents
                new_children = list()
                for _ in range(max_children):
                    p1, p2 = selecao_parental(), selecao_parental()
                    done = False
                    if random.random() < probabilidadeDeCrossover:
                        children = crossover(p1, p2)
                        done = True
                    else:
                        children = [p1[:], p2[:]]
                    for child in children:
                        if random.random() < probabilidadedeMutacao or not done:
                            mutacao(child)
                        new_children.append(child)
                Populacao.extend(new_children)

                # elimina indivíduos de maior custo (objetivo : minimizar custo)
                Populacao.sort(key=lambda q: q[-1])
                del Populacao[PopulationSize:]

                cost_list.append(Populacao[0][-1])
                iteration_count += 1

            end_time = time.process_time() - start_time
            del Populacao[0][-1]
            Tempo_Total += end_time 
            arquivo = open('genetic.txt','a')
            print("Execução %d:" %(i))
            arquivo.write("\nExecucao %d:\n" %(i))
            print("Total de iteracoes: %d\n" %(iteration_count))
            arquivo.write("Total de iteracoes: %d\n" %(iteration_count))
            print("Tempo da execução %d: %s\n"%(i , end_time))
            arquivo.write("Tempo da execucao %d: %s\n"%(i , end_time))
            arquivo.close()
        Tempo_Total = Tempo_Total / 3
        arquivo = open('genetic.txt','a')
        print("\nMedia de tempo de execução: %s\n"%(Tempo_Total))
        arquivo.write("\nMedia de tempo de execucao: %s\n"%(Tempo_Total))
        print("==============================================")
        arquivo.write("==============================================")
        arquivo.close()

    sys.exit()