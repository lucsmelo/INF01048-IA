import random
import sys
import math
from lucas_pedro_tiago_agent.node import Node
from lucas_pedro_tiago_agent.utils import config_parent_import
config_parent_import()
from board import Board

# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.

MAX_DEPTH = 3  # End condition for alpha_beta_pruning.

# The evaluation is made based on the number of pieces the player has,
#   the number of corners that the player owns and number of legal moves.
# Returns an integer, the higher it is, the better the position is.
def evaluate_position(board,color):
    number_of_pieces = board.piece_count[color]
    number_of_moves = len(board.legal_moves(color))
    corners = [board.tiles[0][0],board.tiles[0][7],board.tiles[7][0],board.tiles[7][7]]
    if board.EMPTY in corners:
        return number_of_pieces + 4 * number_of_moves + 20 * corners.count(color) - 20 * corners.count(board.opponent(color))
    return 5 * number_of_pieces + 2 * number_of_moves + 20 * corners.count(color) - 20 * corners.count(board.opponent(color))


def alpha_beta_pruning(node, depth = 1, alpha = -math.inf, beta = math.inf, maximize = True):
    if depth == MAX_DEPTH or len(node.board.legal_moves(node.color)) == 0:
        value = evaluate_position(node.board,node.player_color)  # Must always compute value for the player, even when minimizing (opponent move)
        node.evaluation = value
        return value
    # Alpha beta eval and pruning. 
    expanded = node.expand()
    if maximize:
        value = -math.inf
        for child in expanded:
            value = max(value, alpha_beta_pruning(child, depth + 1, alpha, beta, False))
            if value > alpha:   # Found new best move
                alpha = value 
                node.best_move = child.previous_move    # Will favor the move that generated this child
            if value >= beta:
                break # Beta is pruned.
        return value
    else:
        value = math.inf
        for child in expanded:
            value = min(value, alpha_beta_pruning(child, depth + 1, alpha, beta, True))
            if value < beta:    # Found new best move (for minimization)
                beta = value 
                node.best_move = child.previous_move    # Will favor the move that generated this child
            if value <= alpha:
                break # Alpha is pruned.
        return value


def make_move(the_board, color):
    """
    Returns an Othello move
    :param the_board: a board.Board object with the current game state
    :param color: a character indicating the color to make the move ('B' or 'W')
    :return: (int, int) tuple with x, y indexes of the move (remember: 0 is the first row/column)
    """
    root = Node(the_board, color, None, 0, color, 0)
    alpha_beta_pruning(root, 0, -math.inf, math.inf, True)  # sets the best move into 'root' object

    return root.best_move

