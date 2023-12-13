import unittest
from Board import Board
from Piece import Piece
from Colour import Colour
from Type import Type

class ChessTest(unittest.TestCase):
    
    def test_board_initialization(self):
        """
        Tests whether board is able to be initialized, as well as whether status is able to be initialized.
        This checks that the Type and Colour enum and the Piece class are able to be used.
        """
        board = Board()
        self.assertNotEqual(board.get_status(), None)
        


unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(ChessTest))