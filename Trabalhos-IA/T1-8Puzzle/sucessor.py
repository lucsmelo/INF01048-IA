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
    

teste = Nodo('1234_6785')
a = teste.successor()
print(teste.acao)
print(a)
# Teste de expande
print(teste.__dict__)
for i in teste.expande():
    print(i.__dict__)
