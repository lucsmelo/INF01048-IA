import unittest 
import heuristics

class TestHeuristics(unittest.TestCase):

    # Testing hamming heuristic
    def test_hamming_two(self):
        self.assertEqual(2, heuristics.hamming('1234567_8'))

    def test_hamming_three(self):
        self.assertEqual(3, heuristics.hamming('1234568_7'))

    def test_hamming_several(self):
        self.assertEqual(6, heuristics.hamming('8634521_7'))

    # Testing manhattan heuristic
    def test_manhattan_two(self):
        self.assertEqual(2, heuristics.manhattan('1234567_8'))

    def test_manhattan_four(self):
        self.assertEqual(4, heuristics.manhattan('12345_768'))

    def test_manhattan_several(self):
        crazy_state = '28543_761'
        # crazy_state:
        # 2 8 5
        # 4 3 _
        # 7 6 1
        #
        # Distances by cell:
        # 1 2 2
        # 0 2 1
        # 0 2 4
        #
        # total distance: 1+2+2+0+2+1+0+2+4 = 14
        self.assertEqual(14, heuristics.manhattan(crazy_state))


if __name__ == '__main__':
    unittest.main()
