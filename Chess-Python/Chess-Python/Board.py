import unittest
from Piece import Piece
from Colour import Colour
from Type import Type

class Board:
    
    def __init__(self):
        """
        Construct a new 'Board' object.
        """
        self.__status = [[Piece(Colour.BLACK, Type.ROOK, (0,0), 5.0), Piece(Colour.BLACK, Type.KNIGHT, (0,1), 3.0), Piece(Colour.BLACK, Type.BISHOP, (0,2), 3.25), Piece(Colour.BLACK, Type.QUEEN, (0,3), 9.0), Piece(Colour.BLACK, Type.KING, (0,4), 100.0), Piece(Colour.BLACK, Type.BISHOP, (0,5), 3.25), Piece(Colour.BLACK, Type.KNIGHT, (0,6), 3.0), Piece(Colour.BLACK, Type.ROOK, (0,7), 5.0)],
                        [Piece(Colour.BLACK, Type.PAWN, (1,0), 1.0), Piece(Colour.BLACK, Type.PAWN, (1,1), 1.0), Piece(Colour.BLACK, Type.PAWN, (1,2), 1.0), Piece(Colour.BLACK, Type.PAWN, (1,3), 1.0), Piece(Colour.BLACK, Type.PAWN, (1,4), 1.0), Piece(Colour.BLACK, Type.PAWN, (1,5), 1.0), Piece(Colour.BLACK, Type.PAWN, (1,6), 1.0), Piece(Colour.BLACK, Type.PAWN, (1,7), 1.0)],
                            [None, None ,None, None, None, None, None, None],
                                [None, None ,None, None, None, None, None, None],
                                    [None, None ,None, None, None, None, None, None],
                                        [None, None ,None, None, None, None, None, None],
                                            [Piece(Colour.WHITE, Type.PAWN, (6,0), 1.0), Piece(Colour.WHITE, Type.PAWN, (6,1), 1.0), Piece(Colour.WHITE, Type.PAWN, (6,2), 1.0), Piece(Colour.WHITE, Type.PAWN, (6,3), 1.0), Piece(Colour.WHITE, Type.PAWN, (6,4), 1.0), Piece(Colour.WHITE, Type.PAWN, (6,5), 1.0), Piece(Colour.WHITE, Type.PAWN, (6,6), 1.0), Piece(Colour.WHITE, Type.PAWN, (6,7), 1.0)],
                                                [Piece(Colour.WHITE, Type.ROOK, (7,0), 5.0), Piece(Colour.WHITE, Type.KNIGHT, (7,1), 3.0), Piece(Colour.WHITE, Type.BISHOP, (7,2), 3.25), Piece(Colour.WHITE, Type.QUEEN, (7,3), 9.0), Piece(Colour.WHITE, Type.KING, (7,4), 100.0), Piece(Colour.WHITE, Type.BISHOP, (7,5), 3.25), Piece(Colour.WHITE, Type.KNIGHT, (7,6), 3.0), Piece(Colour.WHITE, Type.ROOK, (7,7), 5.0)]]
        self.__game_over = False
        
    def translate_move(self, desired_move_string_format):
        """
        Translates a user input for a desired move into a usable tuple.
        
        :param desired_move: (String) The user input for a desired move, expected in the form of (A-Z)(1-8).
        :return: (tuple) Translated desired move.
        """
        pass
    
    def get_status(self):
        """
        Returns an array representation of the board.
        
        :return: (Piece []) The status attribute.
        """
        return self.__status
    
    def print_status(self):
        """
        Iterates over status array and prints the character representation of each piece to look like an ASCII board.
        """
        for piece in self.__status:
            if piece == None: print("x")
            else: print(piece.get_char_representation())
            
    def check_move_legality(self, piece, desired_pos):
        """
        Checks whether a user's desired move is legal.
        
        :param piece: (Piece) The piece that the user desires to move.
        :param desired_pos: (tuple) The position the user desires to move a piece to.
        :return: (Boolean) Result of evaluation of legality.
        """
        return False
    
    def check_pawn_move_legality(self, piece, desired_pos):
        """
        Checks whether a user's desired move with a pawn is legal.
        
        :param piece: (Piece) The piece that the user desires to move.
        :param desired_pos: (tuple) The position the user desires to move a piece to.
        :return: (Boolean) Result of evaluation of legality.
        """
        pass
    
    def check_knight_move_legality(self, piece, desired_pos):
        """
        Checks whether a user's desired move with a knight is legal.
        
        :param piece: (Piece) The piece that the user desires to move.
        :param desired_pos: (tuple) The position the user desires to move a piece to.
        :return: (Boolean) Result of evaluation of legality.
        """
        pass
    
    def check_bishop_move_legality(self, piece, desired_pos):
        """
        Checks whether a user's desired move with a bishop is legal.
        
        :param piece: (Piece) The piece that the user desires to move.
        :param desired_pos: (tuple) The position the user desires to move a piece to.
        :return: (Boolean) Result of evaluation of legality.
        """
        pass
    
    def check_rook_move_legality(self, piece, desired_pos):
        """
        Checks whether a user's desired move with a rook is legal.
        
        :param piece: (Piece) The piece that the user desires to move.
        :param desired_pos: (tuple) The position the user desires to move a piece to.
        :return: (Boolean) Result of evaluation of legality.
        """
        pass
    
    def check_queen_move_legality(self, piece, desired_pos):
        """
        Checks whether a user's desired move with a queen is legal.
        
        :param piece: (Piece) The piece that the user desires to move.
        :param desired_pos: (tuple) The position the user desires to move a piece to.
        :return: (Boolean) Result of evaluation of legality.
        """
        pass
    
    def check_king_move_legality(self, piece, desired_pos):
        """
        Checks whether a user's desired move with a king is legal.
        
        :param piece: (Piece) The piece that the user desires to move.
        :param desired_pos: (tuple) The position the user desires to move a piece to.
        :return: (Boolean) Result of evaluation of legality.
        """
        pass
    
    def move_piece(self, piece, desired_pos):
        """
        Moves a piece on the board.
        
        :param piece: (Piece) The piece that the user desires to move.
        :param desired_pos: (tuple) The position the user desires to move a piece to.
        """
        if self.check_move_legality(piece, desired_pos):
            pass
        pass
    