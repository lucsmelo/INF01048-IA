from minimax_alphabeta_pruning_limited import decisao, _MAX_DEPTH

# Quiz da semana 3:
# https://moodle.inf.ufrgs.br/mod/quiz/view.php?id=100630


A = {
    'label': 'A',
    'visited': False,
    'is_terminal': False,
    'heuristic': 8,  # Perfect heuristic, using the value that would be chosen considering children
}
B = {
    'label': 'B',
    'visited': False,
    'is_terminal': False,
    'heuristic': 6,  # Perfect heuristic, using the value that would be chosen considering children
}
C = {
    'label': 'C',
    'visited': False,
    'is_terminal': False,
    'heuristic': 1,  # Perfect heuristic, using the value that would be chosen considering children
}
D = {
    'label': 'D',
    'visited': False,
    'is_terminal': False,
    'heuristic': 8,  # Perfect heuristic, using the value that would be chosen considering children
}
E = {
    'label': 'E',
    'visited': False,
    'is_terminal': False,
    'heuristic': 6,  # Perfect heuristic, using the value that would be chosen considering children
}
F = {
    'label': 'F',
    'visited': False,
    'is_terminal': False,
    'heuristic': 9,  # Perfect heuristic, using the value that would be chosen considering children
}
G = {
    'label': 'G',
    'visited': False,
    'is_terminal': False,
    'heuristic': 2,  # Perfect heuristic, using the value that would be chosen considering children
}
H = {
    'label': 'H',
    'visited': False,
    'is_terminal': False,
    'heuristic': 1,  # Perfect heuristic, using the value that would be chosen considering children
}
I = {
    'label': 'I',
    'visited': False,
    'is_terminal': False,
    'heuristic': 8,  # Perfect heuristic, using the value that would be chosen considering children
}
J = {
    'label': 'J',
    'visited': False,
    'is_terminal': False,
    'heuristic': 9,  # Perfect heuristic, using the value that would be chosen considering children
}
K = {
    'label': 'K',
    'visited': False,
    'is_terminal': True,
    'heuristic': 6,  # Since terminal, heuristic == value
    'value': 4
}
L = {
    'label': 'L',
    'visited': False,
    'is_terminal': True,
    'heuristic': 6,  # Since terminal, heuristic == value
    'value': 6
}
M = {
    'label': 'M',
    'visited': False,
    'is_terminal': True,
    'heuristic': 7,  # Since terminal, heuristic == value
    'value': 7
}
N = {
    'label': 'N',
    'visited': False,
    'is_terminal': True,
    'heuristic': 9,  # Since terminal, heuristic == value
    'value': 9
}
O = {
    'label': 'O',
    'visited': False,
    'is_terminal': True,
    'heuristic': 1,  # Since terminal, heuristic == value
    'value': 1
}
P = {
    'label': 'P',
    'visited': False,
    'is_terminal': True,
    'heuristic': 2,  # Since terminal, heuristic == value
    'value': 2
}
Q = {
    'label': 'Q',
    'visited': False,
    'is_terminal': True,
    'heuristic': 0,  # Since terminal, heuristic == value
    'value': 0
}
R = {
    'label': 'R',
    'visited': False,
    'is_terminal': True,
    'heuristic': 1,  # Since terminal, heuristic == value
    'value': 1
}
S = {
    'label': 'S',
    'visited': False,
    'is_terminal': True,
    'heuristic': 8,  # Since terminal, heuristic == value
    'value': 8
}
T = {
    'label': 'T',
    'visited': False,
    'is_terminal': True,
    'heuristic': 1,  # Since terminal, heuristic == value
    'value': 1
}
U = {
    'label': 'U',
    'visited': False,
    'is_terminal': True,
    'heuristic': 9,  # Since terminal, heuristic == value
    'value': 9
}
V = {
    'label': 'V',
    'visited': False,
    'is_terminal': True,
    'heuristic': 2,  # Since terminal, heuristic == value
    'value': 2
}

A['succ'] = {
    'left': B,
    'center': C,
    'right': D
}
B['succ'] = {
    'left': E,
    'right': F
}
C['succ'] = {
    'left': H,
    'right': H
}
D['succ'] = {
    'left': I,
    'right': J
}
E['succ'] = {
    'left': K,
    'right': L
}
F['succ'] = {
    'left': M,
    'right': N
}
G['succ'] = {
    'left': O,
    'right': P
}
H['succ'] = {
    'left': Q,
    'right': R
}
I['succ'] = {
    'left': S,
    'right': T
}
J['succ'] = {
    'left': U,
    'right': V
}


all_nodes = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V]

decision = decisao(A)

print(' ')

print(f'Best choice from root node: go {decision}')

#all_visited = [n for n in all_nodes if n['visited']]
not_visited = [n for n in all_nodes if not n['visited']]
print(f'Number of nodes not visited using maximum depth {_MAX_DEPTH}:  {len(not_visited)}')
print('Change property _MAX_DEPTH on minimax_alphabeta_pruning_limited.py to have different number of ignored nodes')

#[print(n['label']) for n in all_visited]
#[print(n['label']) for n in not_visited]

