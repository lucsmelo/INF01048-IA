from typing import List

# Indices that form the edges, 
# to help when checking movements.
_RIGHT_EDGE = [2, 5, 8]
_LEFT_EDGE = [0, 3, 6]
_TOP_EDGE = [0, 1, 2]
_BOTTOM_EDGE = [6, 7, 8]
# For reference:
# 0 1 2
# 3 4 5
# 6 7 8


def move(current: str, action: str) -> str: 
    space_pos = current.find('_')
    replace_pos = space_pos

    if action == 'direita':
        if space_pos not in _RIGHT_EDGE:
            replace_pos = space_pos + 1
    if action == 'esquerda':
        if space_pos not in _LEFT_EDGE:
            replace_pos = space_pos - 1
    if action == 'abaixo':
        if space_pos not in _BOTTOM_EDGE:
            replace_pos = space_pos + 3
    if action == 'acima':
        if space_pos not in _TOP_EDGE:
            replace_pos = space_pos - 3

    char_to_move = current[replace_pos]
    result = current[:replace_pos] + '_' + current[replace_pos+1:]  # Move space
    result = result[:space_pos] + char_to_move + result[space_pos+1:]  # Move char

    return result


def apply_sequence(current: str, actions: List[str]) -> str:
    result = current 
    for action in actions:
        result = move(result, action)
    return result

