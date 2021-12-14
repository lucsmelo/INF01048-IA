class Nodo:

    def __init__(self, estado, pai=None, acao=None, custo=0):

        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo

    def split_string(self):
        liststate = []
        for char in self.estado:
            liststate.append(char)
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
            options.append(('Direita', self.swap(space_pos, space_pos + 1)))   
        if space_pos != 0 and space_pos != 3 and space_pos != 6:
            # self.acao = 'Esquerda'
            # options.append((self.acao, self.swap(space_pos, space_pos - 1)))  # -->Esquerda
            options.append(('Esquerda', self.swap(space_pos, space_pos - 1)))   
        if space_pos < 6:
            # self.acao = 'Abaixo'
            # options.append((self.acao, self.swap(space_pos, space_pos + 3)))  # -->Abaixo
            options.append(('Abaixo', self.swap(space_pos, space_pos + 3)))  
        if space_pos > 2:
            # self.acao = 'Acima'
            # options.append((self.acao, self.swap(space_pos, space_pos - 3)))  # -->Acima
            options.append(('Acima', self.swap(space_pos, space_pos - 3)))  

        return options

    def expande(self):
        """
        Recebe um nodo (objeto da classe Nodo) e retorna um iterable de nodos.
        Cada nodo do iterable é contém um estado sucessor do nó recebido.
        :param nodo: objeto da classe Nodo
        :return: array de nodos
        """
        succ = self.successor()
        return [ Nodo(s[1],self,s[0],self.custo + 1) for s in succ ] 


def make_parent_list(node):
    """
    Auxiliary function that can be used to trace a path back to the origin node from a leaf node.
    Returns an ordered list that goes from the root to the leaf.

    :node: the leaf node.
    """
    if node.pai == None:
        return [node]
    else:
        return make_parent_list(node.pai) + [node]

def dfs(estado):
    x = set() # Explorados
    f = [Nodo(estado)] # Fronteira em pilha.
    caminho = [] # Nodos no caminho do filho ao pai.
    while len(f) > 0:
        v = f.pop()
        if v.estado == '12345678_':
            while v.pai is not None:
                caminho.append((v.acao))
                v = v.pai
            return caminho
        if not v.estado in x:
            x.add(v.estado)
            f.extend(v.expande())
    return None
        
teste = Nodo('1234567_8')
a = teste.successor()
print(teste.acao)
print(a)
# Teste de expande
caminho, custo, total_visitados = dfs('2_3541687')
print(caminho)
print(custo)
print(total_visitados)