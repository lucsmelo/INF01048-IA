from lucas_pedro_tiago_agent.utils import config_parent_import
config_parent_import()
from board import Board
import copy

class Node:

    def __init__(self, board, player_color, parent = None, cost = 1, color = Board.WHITE, evaluation = 0, previous_move = (-1,-1), best_move = (-1,-1)):
        self.board = board
        self.player_color = player_color  # Needs this as the algorithm always min/max from the point of view of the player
        self.parent = parent
        self.cost = cost
        self.color = color # Color that will make the next move, not the one that led to this state.
        self.eval = evaluation # Evaluation of the board for this state 
        self.previous_move = previous_move  # Move taken on parent to get to this node
        self.best_move = best_move  # The best next move, to be finally set once minimax algorithm finds it
    
    # Will raise exception trying to expand None.
    # Returns a list of new nodes.
    def expand(self):
        result = []
        moves = self.board.legal_moves(self.color)
        for move in moves:
            board = copy.deepcopy(self.board)
            board.process_move(move,self.color)
            child = Node(board,self.color,self,self.cost + 1,board.opponent(self.color), 0, move, (-1,-1))
            result.append(child)
        return result
