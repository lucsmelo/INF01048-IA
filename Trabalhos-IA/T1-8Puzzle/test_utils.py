import unittest 
import utils

class TestUtils(unittest.TestCase):

    # Testing move method
    def test_move_right(self):
        current_state = '1234567_8'
        self.assertEqual('12345678_', utils.move(current_state, 'direita'))
    
    def test_move_right_stops_at_edge_top(self):
        current_state = '12_345678'
        self.assertEqual('12_345678', utils.move(current_state, 'direita'))

    def test_move_right_stops_at_edge_middle(self):
        current_state = '12345_678'
        self.assertEqual('12345_678', utils.move(current_state, 'direita'))

    def test_move_right_stops_at_edge_bottom(self):
        current_state = '12345678_'
        self.assertEqual('12345678_', utils.move(current_state, 'direita'))

    def test_move_left(self):
        current_state = '1234567_8'
        self.assertEqual('123456_78', utils.move(current_state, 'esquerda'))

    def test_move_left_stops_at_edge_top(self):
        current_state = '_12345678'
        self.assertEqual('_12345678', utils.move(current_state, 'esquerda'))

    def test_move_left_stops_at_edge_middle(self):
        current_state = '123_45678'
        self.assertEqual('123_45678', utils.move(current_state, 'esquerda'))

    def test_move_left_stops_at_edge_bottom(self):
        current_state = '123456_78'
        self.assertEqual('123456_78', utils.move(current_state, 'esquerda'))

    def test_move_down(self):
        current_state = '12_345678'
        self.assertEqual('12534_678', utils.move(current_state, 'abaixo'))

    def test_move_down_stops_at_edge_left(self):
        current_state = '123456_78'
        self.assertEqual('123456_78', utils.move(current_state, 'abaixo'))

    def test_move_down_stops_at_edge_center(self):
        current_state = '1234567_8'
        self.assertEqual('1234567_8', utils.move(current_state, 'abaixo'))

    def test_move_down_stops_at_edge_right(self):
        current_state = '12345678_'
        self.assertEqual('12345678_', utils.move(current_state, 'abaixo'))

    def test_move_up(self):
        current_state = '1234_5678'
        self.assertEqual('1_3425678', utils.move(current_state, 'acima'))

    def test_move_up_stops_at_edge_left(self):
        current_state = '_12345678'
        self.assertEqual('_12345678', utils.move(current_state, 'acima'))

    def test_move_up_stops_at_edge_center(self):
        current_state = '1_2345678'
        self.assertEqual('1_2345678', utils.move(current_state, 'acima'))

    def test_move_up_stops_at_edge_right(self):
        current_state = '12_345678'
        self.assertEqual('12_345678', utils.move(current_state, 'acima'))

    # Testing apply_sequence method
    def test_apply_sequence_empty(self):
        current_state = '12_345678'
        self.assertEqual('12_345678', utils.apply_sequence(current_state, []))

    def test_apply_sequence_one_move(self):
        current_state = '12_345678'
        sequence = ['esquerda']
        self.assertEqual('1_2345678', utils.apply_sequence(current_state, sequence))

    def test_apply_sequence_two_moves_distinct(self):
        current_state = '12_345678'
        sequence = ['esquerda', 'esquerda']
        self.assertEqual('_12345678', utils.apply_sequence(current_state, sequence))

    def test_apply_sequence_two_moves_returning(self):
        current_state = '12_345678'
        sequence = ['esquerda', 'direita']
        self.assertEqual('12_345678', utils.apply_sequence(current_state, sequence))




if __name__ == '__main__':
    unittest.main()
