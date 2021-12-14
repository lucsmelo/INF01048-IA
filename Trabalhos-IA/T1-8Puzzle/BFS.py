import collections
from collections import deque


class Nodo:

    def __init__(self, estado, pai=None, acao=None, custo=0):

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

    def successor(self):
        options = []
        space_pos = self.estado.find('_')

        if space_pos != 2 and space_pos != 5 and space_pos != 8:
            # self.acao = 'Direita'
            # options.append((self.acao, self.swap(space_pos, space_pos + 1)))  # -->Direita
            options.append(('direita', self.swap(space_pos, space_pos + 1)))  # -->Direita
        if space_pos != 0 and space_pos != 3 and space_pos != 6:
            # self.acao = 'Esquerda'
            # options.append((self.acao, self.swap(space_pos, space_pos - 1)))  # -->Esquerda
            options.append(('esquerda', self.swap(space_pos, space_pos - 1)))  # -->Esquerda
        if space_pos < 6:
            # self.acao = 'Abaixo'
            # options.append((self.acao, self.swap(space_pos, space_pos + 3)))  # -->Abaixo
            options.append(('abaixo', self.swap(space_pos, space_pos + 3)))  # -->Abaixo
        if space_pos > 2:
            # self.acao = 'Acima'
            # options.append((self.acao, self.swap(space_pos, space_pos - 3)))  # -->Acima
            options.append(('acima', self.swap(space_pos, space_pos - 3)))  # -->Acima

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


def BFS(estado):
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
            return path
        if current_state.estado not in explored:
            explored.add(current_state.estado)
            succ = current_state.expande()
            [frontier.append(s) for s in succ]


total_path = BFS('2_3541687')
print(f'caminho: {total_path} custo: {len(total_path)}')
inexistent_path=BFS('185423_67')
if inexistent_path is not  None:
    print(f'caminho: {inexistent_path} custo:{len(inexistent_path)} ')
else:
    print(f'caminho: {inexistent_path}')