from enum import Enum

class Type(Enum):
    """
    Enumeration representing the possible types for a piece and their standard chess notation character representation.

    Attributes:
        PAWN: Represents a pawn, with the character representation of 'P' to be used for printing the board.
        KNIGHT: Represents a knight, with the character representation of 'N' to be used for printing the board (K is taken by the king).
        BISHOP: Represents a bishop, with the character representation of 'B' to be used for printing the board.
        ROOK: Represents a rook, with the character representation of 'R' to be used for printing the board.
        QUEEN: Represents a queen, with the character representation of 'Q' to be used for printing the board.
        KING: Represents a king, with the character representation of 'K' to be used for printing the board.
    """
    PAWN = "P"
    KNIGHT = "N"
    BISHOP = "B"
    ROOK = "R"
    QUEEN = "Q"
    KING = "K"
