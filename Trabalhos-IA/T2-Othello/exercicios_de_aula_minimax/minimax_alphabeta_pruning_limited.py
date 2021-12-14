import math

_MAX_DEPTH = 3


# Helper
def get_succ(node):
    return node['succ']

def teste_de_corte(node):
    return node['depth'] >= _MAX_DEPTH

def avalia(node):
    return node['heuristic'] 

def decisao(node):
    node['depth'] = 0
    v = valor_MAX(node, -math.inf, math.inf)
    succs = get_succ(node)
    for a in succs:
        n = succs[a]
        if n['value'] == v:
            return a

def valor_MAX(node, alpha, beta):
    print(f'MAX examining node {node["label"]}')
    node['visited'] = True
    if node['is_terminal']:
        return node['value']
    if teste_de_corte(node):
        evaluated_value = avalia(node)
        node['value'] = evaluated_value
        return evaluated_value
    succs = get_succ(node)
    for a in succs:
        n = succs[a]
        n['depth'] = node['depth'] + 1
        v = valor_MIN(n, alpha, beta)
        alpha = max(alpha, v)
        if alpha > beta:
            break
    node['value'] = alpha
    return alpha

def valor_MIN(node, alpha, beta):
    print(f'MIN examining node {node["label"]}')
    node['visited'] = True
    if node['is_terminal']:
        return node['value']
    if teste_de_corte(node):
        evaluated_value = avalia(node)
        node['value'] = evaluated_value
        return evaluated_value
    succs = get_succ(node)
    for a in succs:
        n = succs[a]
        n['depth'] = node['depth'] + 1
        v = valor_MAX(n, alpha, beta)
        beta = min(beta, v)
        if beta < alpha:
            break
    node['value'] = beta
    return beta


if __name__ == '__main__':
    print('Run file ex_alphabeta_pruning_limited_exercise.py instead!')