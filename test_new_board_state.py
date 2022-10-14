import unittest

from game_of_life import new_board_state


class TestBoard(unittest.TestCase):
    def test_new_board_state(self):
        table = [[1, 1, 1, 0], [1, 0, 1, 1], [0, 0, 0, 1], [0, 1, 0, 0], [0, 1, 1, 0]]
        new_table = new_board_state(table)
        self.assertEqual(new_table,
                         [[1, 0, 1, 1], [1, 0, 0, 1], [0, 1, 0, 1], [0, 1, 0, 0], [0, 1, 1, 0]])


if __name__ == '__main__':
    unittest.main()
