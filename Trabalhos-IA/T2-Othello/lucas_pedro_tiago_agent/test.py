from utils import config_parent_import
from agent import alpha_beta_pruning
config_parent_import()
from board import Board
from lucas_pedro_tiago_agent.node import Node

bd = Board()
bd.print_board()
bd.process_move((5,3),Board.WHITE)
bd.print_board()
bd.process_move((3,2),Board.BLACK)
bd.print_board()
abp = alpha_beta_pruning(Node(bd))
