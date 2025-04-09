import unittest
from game.solitaire import Solitaire

class TestSolitaire(unittest.TestCase):

    def setUp(self):
        self.game = Solitaire()
        self.game.create_deck()
        self.game.construct_puzzle()
        self.game.create_stock()

    def test_draw_card(self):
        stock_length = len(self.game.stock)
        self.game.draw_card()
        self.assertEqual(len(self.game.waste), 1)
        self.assertEqual(len(self.game.stock), stock_length - 1)
