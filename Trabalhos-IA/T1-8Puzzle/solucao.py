from typing import List
from queue import PriorityQueue
from time import time

from heuristics import hamming, manhattan

_expanded_in_last_successful_run = 0
_time_taken_on_last_successful_run = 0
_cost_on_last_successful_run = 0


class Nodo:
    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """

    def __init__(self, estado, pai, acao, custo):
        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo

    def split_string(self):  
        liststate = []
        [liststate.append(c) for c in self.estado]
        return liststate

    def swap(self, pos1, pos2):  
        liststate = self.split_string()
        liststate[pos1], liststate[pos2] = liststate[pos2], liststate[pos1]
        return ''.join(map(str, liststate))

    def make_actions_list(self) -> List[str]:
        """
        Returns a list with all the actions taken to reach this node
        :param self: Object of class Nodo
        :return: list of strings representing actions
        """
        current = self
        path = []
        while current.pai is not None:
            path.insert(0, current.acao)
            current = current.pai
        return path

    def successor(self):  
        options = []
        space_pos = self.estado.find('_')

        if space_pos != 2 and space_pos != 5 and space_pos != 8:  # --> Direita
            options.append(('direita', self.swap(space_pos, space_pos + 1)))
        if space_pos != 0 and space_pos != 3 and space_pos != 6:  # -->Esquerda
            options.append(('esquerda', self.swap(space_pos, space_pos - 1)))
        if space_pos < 6:  # -->Abaixo
            options.append(('abaixo', self.swap(space_pos, space_pos + 3)))
        if space_pos > 2:  # -->Acima
            options.append(('acima', self.swap(space_pos, space_pos - 3)))

        return options

    def expande(self):  
        """
        Recebe um nodo (objeto da classe Nodo) e retorna um iterable de nodos.
        Cada nodo do iterable é contém um estado sucessor do nó recebido.
        :param nodo: objeto da classe Nodo
        :return: array de nodos
        """
        succ = self.successor()
        return [Nodo(s[1], self, s[0], self.custo + 1) for s in succ]


def sucessor(estado):
    """
    Recebe um estado (string) e retorna uma lista de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """
    node = Nodo(estado, None, None, 0)  
    return node.successor()  


def expande(nodo):
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um iterable de nodos.
    Cada nodo do iterable é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """
    succ = nodo.successor()
    return [Nodo(s[1], nodo, s[0], nodo.custo + 1) for s in succ]


def bfs(estado):
    """
    Recebe um nodo (objeto da classe Nodo) e retorna uma lista com o caminho s-v.
    :param estado:string referente ao estado inicial
    :return: Lista com caminho s-v
    """

    explored = set()  # Garante que nós repetidos não entrem na fronteira
    frontier = [Nodo(estado, None, None, 0)]
    path = []
    # print(F[0].estado)
    while True:
        if len(frontier) == 0:
            return None
        current_state = frontier.pop(0)
        if current_state.estado == '12345678_':

            custo = current_state.custo
            while current_state.pai is not None:
                path.append(current_state.acao)
                current_state = current_state.pai
            path.reverse()
            return path
        if current_state.estado not in explored:
            explored.add(current_state.estado)
            succ = current_state.expande()
            [frontier.append(s) for s in succ]


def dfs(estado):
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """

    x = set() # Explorados
    f = [Nodo(estado, None, None, 0)] # Fronteira em pilha.
    caminho = [] # Nodos no caminho do filho ao pai.
    while len(f) > 0:
        v = f.pop()
        if v.estado == '12345678_':
            while v.pai is not None:
                caminho.append((v.acao))
                v = v.pai
            caminho.reverse()
            return caminho
        if not v.estado in x:
            x.add(v.estado)
            f.extend(v.expande())
    return None


def astar(estado: str, heuristic: 'function') -> List[str]:
    """
    Given a state (string), and a heuristic (function), executes A* search with h(n) = heuristic(n) and returns
    a list of actions that take the given state to the winning state ("12345678_")
    If there is no solution starting from the given state, returns None
    :param estado: str
    :param heuristic: function
    :return: list of strings representing actions
    """
    start_time = time()
    explored_states = set()
    frontier = PriorityQueue()

    starting_node = Nodo(estado, None, None, 0)

    # Vamos usar uma priority queue com tuplas no formato:
    # ( prioridade , id_do_nodo , nodo)
    # onde 'prioridade' eh f(v), o custo da funcao para o nodo,
    #   calculado com a formula f(v) = custo_real + custo_na_heuristica
    # Assim, 'prioridade' eh o que determinara qual nodo sera tirado da fila.
    # O motivo para ter 'id_do_nodo' ali eh por detalhes internos da PriorityQueue,
    # para maiores informacoes, checar o link abaixo:
    # https://stackoverflow.com/questions/53554199/heapq-push-typeerror-not-supported-between-instances
    frontier.put((starting_node.custo + heuristic(starting_node.estado), id(starting_node), starting_node))

    while not frontier.empty():
        _, _, current = frontier.get()

        if current.estado == '12345678_':
            global _expanded_in_last_successful_run, _cost_on_last_successful_run, _time_taken_on_last_successful_run
            _expanded_in_last_successful_run = len(explored_states)
            _cost_on_last_successful_run = current.custo
            _time_taken_on_last_successful_run = time() - start_time
            return current.make_actions_list()  # Deu bom

        if not current.estado in explored_states:
            explored_states.add(current.estado)
            successors = current.expande()
            for succ in successors:
                cost_function = succ.custo + heuristic(succ.estado)
                frontier.put((cost_function, id(succ), succ))

    return None  # Deu ruim


def astar_hamming(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    return astar(estado, hamming)


def astar_manhattan(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    return astar(estado, manhattan)


if __name__ == '__main__':
    benchmark_state = '2_3541687'

    # Getting data for A* Hamming
    path_hamming = astar_hamming(benchmark_state)
    print(f'Data for A* Hamming')
    print(f'Nodes expanded: {_expanded_in_last_successful_run}')
    print(f'Time: {_time_taken_on_last_successful_run}')
    print(f'Cost of solution: {_cost_on_last_successful_run}')
    print(f'Length of path found: {len(path_hamming)}')
    print('')

    # Getting data for A* Manhattan
    path_manhattan = astar_manhattan(benchmark_state)
    print(f'Data for A* Manhattan')
    print(f'Nodes expanded: {_expanded_in_last_successful_run}')
    print(f'Time: {_time_taken_on_last_successful_run}')
    print(f'Cost of solution: {_cost_on_last_successful_run}')
    print(f'Length of path found: {len(path_manhattan)}')
    print('')
