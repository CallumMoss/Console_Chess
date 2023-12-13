class Piece:
    """
    Encapsulates necessary variables for a Piece.
    """
    def __init__(self, colour, type, pos, typical_value):
        """
        Construct a new 'Piece' object.
        
        :param colour: (Colour) The colour of the piece, chosen from Colour enumeration.
        :param type: (Type) The type of piece, chosen from Type enumeration.
        :param pos: (tuple) The position of the piece on the board.
        :param char_representation: (char) The character representation of the piece in chess notation.
        :param typical_value: (float) The accepted value of a given piece at the start of the game.
        """
        self.__colour = colour
        self.__type = type
        self.__pos = pos
        self.__typical_value = typical_value
        self.__char_representation = type.value



