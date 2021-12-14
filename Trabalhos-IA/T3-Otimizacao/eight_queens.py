import random

import numpy as np
from matplotlib import pyplot as plt

_GENERATE_GRAPH = False
max_v = []
mean_v = []
min_v = []


def evaluate(individual):
    """
    Recebe um indivíduo (lista de inteiros) e retorna o número de ataques
    entre rainhas na configuração especificada pelo indivíduo.
    Por exemplo, no individuo [2,2,4,8,1,6,3,4], o número de ataques é 9.

    :param individual:list
    :return:int numero de ataques entre rainhas no individuo recebido
    """
    # Idea:
    # Starting from the leftmost column, check for rightward conflicts for this queen,
    #   and then proceed to do the same for the next column to the right, until next-to-last one.
    # Check for conflicts only to the right, in order to avoid duplicated conflicts.
    #   Also, this is why it is not needed to check the last column:
    #     by the time the algorithm reaches there, all conflicts with the last queen were already found.
    # There is also no need to check for conflicts up or down the same column, since only one queen can occupy it
    #   by the very structure of the entry.
    # The variable 'pos' checks for conflicts on the same line, 'up' on upward diagonal and 'down' on downwards diagonal.
    # The algorithm is bounded only on the right-most column, but not on top or bottom (that is, it can
    #   check if there is a 'conflict' with a queen on lines -1 or 12, for instance), but this does not
    #   interfere with the result, assuming valid entries. If an invalid entry is used (with queens 'outside' of the
    #   grid), the answer might have some weirdness to it - proportional to the weirdness of the entry.
    #   Here, we follow the Garbage In, Garbage Out philosophy.

    conflicts = 0

    for i in range(7):  # traverses each column EXCEPT last one

        pos = individual[i]  # position of queen on this column (the one looking for conflicts)
        up = pos  # will use to check conflicts on upwards diagonal
        down = pos  # will use to check conflicts on downwards diagonal

        for j in range(i + 1, 8):  # traverses every column to the right looking for conflicts
            up += 1  # upwards diagonal: one to the right, one up
            down -= 1  # downwards diagonal: one to the right, one down

            queen_of_this_column = individual[j]  # position of queen on this column (the one possibly conflicting)

            if queen_of_this_column == up or queen_of_this_column == pos or queen_of_this_column == down:
                conflicts += 1

    return conflicts


def tournament(participants):
    """
    Recebe uma lista com vários indivíduos e retorna o melhor deles, com relação
    ao numero de conflitos
    :param participants:list - lista de indivíduos
    :return:list melhor individuo da lista recebida
    """
    lst_conflitos = [evaluate(x) for x in participants]
    # print(lst_conflitos)
    index = lst_conflitos.index(min(lst_conflitos))
    # print(participants[index])
    return participants[index]


def crossover(parent1, parent2, index):
    """
    Realiza o crossover de um ponto: recebe dois indivíduos e o ponto de
    cruzamento (indice) a partir do qual os genes serão trocados. Retorna os
    dois indivíduos com o material genético trocado.
    Por exemplo, a chamada: crossover([2,4,7,4,8,5,5,2], [3,2,7,5,2,4,1,1], 3)
    deve retornar [2,4,7,5,2,4,1,1], [3,2,7,4,8,5,5,2].
    A ordem dos dois indivíduos retornados não é importante
    (o retorno [3,2,7,4,8,5,5,2], [2,4,7,5,2,4,1,1] também está correto).
    :param parent1:list
    :param parent2:list
    :param index:int
    :return:list,list
    """
    son1 = parent1[:index] + parent2[index:]
    son2 = parent2[:index] + parent1[index:]
    return son1, son2


def mutate(individual, m):
    """
    Recebe um indivíduo e a probabilidade de mutação (m).
    Caso random() < m, sorteia uma posição aleatória do indivíduo e
    coloca nela um número aleatório entre 1 e 8 (inclusive).
    :param individual:list
    :param m:int - probabilidade de mutacao
    :return:list - individuo apos mutacao (ou intacto, caso a prob. de mutacao nao seja satisfeita)
    """
    if random.random() < m:
        random_pos = random.randint(1, 8)
        random_number = random.randint(1, 8)
        individual[random_pos - 1] = random_number
        # print(random_pos,random_number,individual)
    return individual


def _gen_vec(n):
    """
       Gera um vetor de 8 elementos n vezes
        :param n:int

        :return:list -Lista de indivíduos gerados aleatórios
        """
    lst = []
    lst1 = []
    for i in range(n):
        for j in range(8):
            lst1.append(random.randint(1, 8))
        lst.append(lst1)
        lst1 = []
    return lst


def _gen_gra(max, mean, min, x_tick):
    labels = [x_tick + 1 for x_tick in x_tick]
    fig, ax = plt.subplots()
    ax.set_xticks(x_tick)
    ax.set_xticklabels(labels)

    ax.plot(max)
    ax.plot(mean)
    ax.plot(min)

    ax.get_lines()[0].set_color("green")
    ax.get_lines()[1].set_color("blue")
    ax.get_lines()[2].set_color("red")
    ax.legend(['MAX','MEAN','MIN'])

def run_ga(g, n, k, m, e):
    """
    Executa o algoritmo genético e retorna o indivíduo com o menor número de ataques entre rainhas
    :param g:int - numero de gerações
    :param n:int - numero de individuos
    :param k:int - numero de participantes do torneio
    :param m:float - probabilidade de mutação (entre 0 e 1, inclusive)
    :param e:bool - se vai haver elitismo
    :return:list - melhor individuo encontrado
    """
    p = _gen_vec(n)
    p_ = []
    for i in range(g):

        if e:
            p_.append(tournament(p))
        else:
            p_=[]

        while len(p_) < n:
            p1 = tournament(random.sample(p, k))
            p2 = tournament(random.sample(p, k))  # Meio em dúvida se tiro o p1, mas corre o risco de dar erro no sample
            o1, o2 = crossover(p1, p2, random.randint(0, 7))
            o1 = mutate(o1, m)
            o2 = mutate(o2, m)
            p_.append(o1)
            p_.append(o2)

        p = p_

        if _GENERATE_GRAPH:
            lst_conflitos = [evaluate(x) for x in p]
            max_v.append(max(lst_conflitos))
            mean_v.append(np.mean(lst_conflitos))
            min_v.append(min(lst_conflitos))

    if _GENERATE_GRAPH:
        x = list(range(g))
        _gen_gra(max_v, mean_v, min_v, x)
        plt.show()

    return tournament(p)

max_v.clear()
mean_v.clear()
min_v.clear()


if __name__ == '__main__':
    _GENERATE_GRAPH = True
    reference_execution = run_ga(35, 32, 17, 0.81, False)
    print(reference_execution, evaluate(reference_execution))