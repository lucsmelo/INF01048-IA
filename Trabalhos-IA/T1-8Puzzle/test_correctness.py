import unittest 
import solucao
import utils  

_WINNING_STATE = '12345678_'

class TestCorrectness(unittest.TestCase):

    # Testing bfs
    def test_bfs_trivial(self):
        initial_state = '12345678_'
        path = solucao.bfs(initial_state)
        final_state = utils.apply_sequence(initial_state, path)
        self.assertEqual(_WINNING_STATE, final_state)

    def test_bfs_easy(self):
        initial_state = '_23146758'
        path = solucao.bfs(initial_state)
        final_state = utils.apply_sequence(initial_state, path)
        self.assertEqual(_WINNING_STATE, final_state)

    def test_bfs_hard(self):
        initial_state = '2_3541687'
        path = solucao.bfs(initial_state)
        final_state = utils.apply_sequence(initial_state, path)
        self.assertEqual(_WINNING_STATE, final_state)

    def test_bfs_impossible(self):
        initial_state = '185423_67'
        path = solucao.bfs(initial_state)
        self.assertEqual(None, path)

    # Testing dfs
    def test_dfs_trivial(self):
        initial_state = '12345678_'
        path = solucao.dfs(initial_state)
        final_state = utils.apply_sequence(initial_state, path)
        self.assertEqual(_WINNING_STATE, final_state)

    def test_dfs_easy(self):
        initial_state = '_23146758'
        path = solucao.dfs(initial_state)
        final_state = utils.apply_sequence(initial_state, path)
        self.assertEqual(_WINNING_STATE, final_state)

    def test_dfs_hard(self):
        initial_state = '2_3541687'
        path = solucao.dfs(initial_state)
        final_state = utils.apply_sequence(initial_state, path)
        self.assertEqual(_WINNING_STATE, final_state)

    def test_dfs_impossible(self):
        initial_state = '185423_67'
        path = solucao.dfs(initial_state)
        self.assertEqual(None, path)

    # Testing astar hamming
    def test_astar_hamming_trivial(self):
        initial_state = '12345678_'
        path = solucao.astar_hamming(initial_state)
        final_state = utils.apply_sequence(initial_state, path)
        self.assertEqual(_WINNING_STATE, final_state)

    def test_astar_hamming_easy(self):
        initial_state = '_23146758'
        path = solucao.astar_hamming(initial_state)
        final_state = utils.apply_sequence(initial_state, path)
        self.assertEqual(_WINNING_STATE, final_state)

    def test_astar_hamming_hard(self):
        initial_state = '2_3541687'
        path = solucao.astar_hamming(initial_state)
        final_state = utils.apply_sequence(initial_state, path)
        self.assertEqual(_WINNING_STATE, final_state)

    def test_astar_hamming_impossible(self):
        initial_state = '185423_67'
        path = solucao.astar_hamming(initial_state)
        self.assertEqual(None, path)

    # Testing astar manhattan
    def test_astar_manhattan_trivial(self):
        initial_state = '12345678_'
        path = solucao.astar_manhattan(initial_state)
        final_state = utils.apply_sequence(initial_state, path)
        self.assertEqual(_WINNING_STATE, final_state)

    def test_astar_manhattan_easy(self):
        initial_state = '_23146758'
        path = solucao.astar_manhattan(initial_state)
        final_state = utils.apply_sequence(initial_state, path)
        self.assertEqual(_WINNING_STATE, final_state)

    def test_astar_manhattan_hard(self):
        initial_state = '2_3541687'
        path = solucao.astar_manhattan(initial_state)
        final_state = utils.apply_sequence(initial_state, path)
        self.assertEqual(_WINNING_STATE, final_state)

    def test_astar_manhattan_impossible(self):
        initial_state = '185423_67'
        path = solucao.astar_manhattan(initial_state)
        self.assertEqual(None, path)


if __name__ == '__main__':
    unittest.main()