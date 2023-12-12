import unittest

class ChessTest(unittest.TestCase):
    def board_initialization(self):
        board = Board()
        piece = Piece(Colour.WHITE, Type.PAWN, 1.0)
        assert board.getStatus() == [[Piece(Colour.BLACK, Type.ROOK, (0,0), 5.0), Piece(Colour.BLACK, Type.KNIGHT, (0,1), 3.0), Piece(Colour.BLACK, Type.BISHOP, (0,2), 3.25), Piece(Colour.BLACK, Type.QUEEN, (0,3), 9.0), Piece(Colour.BLACK, Type.KING, (0,4), 100.0), Piece(Colour.BLACK, Type.BISHOP, (0,5), 3.25), Piece(Colour.BLACK, Type.KNIGHT, (0,6), 3.0), Piece(Colour.BLACK, Type.ROOK, (0,7), 5.0)],
                        [Piece(Colour.BLACK, Type.PAWN, (1,0), 1.0), Piece(Colour.BLACK, Type.PAWN, (1,1), 1.0), Piece(Colour.BLACK, Type.PAWN, (1,2), 1.0), Piece(Colour.BLACK, Type.PAWN, (1,3), 1.0), Piece(Colour.BLACK, Type.PAWN, (1,4), 1.0), Piece(Colour.BLACK, Type.PAWN, (1,5), 1.0), Piece(Colour.BLACK, Type.PAWN, (1,6), 1.0), Piece(Colour.BLACK, Type.PAWN, (1,7), 1.0)],
                            [None, None ,None, None, None, None, None, None],
                                [None, None ,None, None, None, None, None, None],
                                    [None, None ,None, None, None, None, None, None],
                                        [None, None ,None, None, None, None, None, None],
                                            [Piece(Colour.WHITE, Type.PAWN, (6,0), 1.0), Piece(Colour.WHITE, Type.PAWN, (6,1), 1.0), Piece(Colour.WHITE, Type.PAWN, (6,2), 1.0), Piece(Colour.WHITE, Type.PAWN, (6,3), 1.0), Piece(Colour.WHITE, Type.PAWN, (6,4), 1.0), Piece(Colour.WHITE, Type.PAWN, (6,5), 1.0), Piece(Colour.WHITE, Type.PAWN, (6,6), 1.0), Piece(Colour.WHITE, Type.PAWN, (6,7), 1.0)],
                                                [Piece(Colour.WHITE, Type.ROOK, (7,0), 5.0), Piece(Colour.WHITE, Type.KNIGHT, (7,1), 3.0), Piece(Colour.WHITE, Type.BISHOP, (7,2), 3.25), Piece(Colour.WHITE, Type.QUEEN, (7,3), 9.0), Piece(Colour.WHITE, Type.KING, (7,4), 100.0), Piece(Colour.WHITE, Type.BISHOP, (7,5), 3.25), Piece(Colour.WHITE, Type.KNIGHT, (7,6), 3.0), Piece(Colour.WHITE, Type.ROOK, (7,7), 5.0)]]


if __name__ == '__main__':
    unittest.main()
