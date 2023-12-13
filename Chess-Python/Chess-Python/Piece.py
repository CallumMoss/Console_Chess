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

    def get_colour(self):
        """
        Returns the piece colour.
        
        :return: (Colour) The piece colour.
        """
        return self.__colour
    
    def get_type(self):
        """
        Returns the piece type.
        
        :return: (Piece) The piece type.
        """
        return self.__type

    def get_pos(self):
        """
        Returns the piece position.
        
        :return: (tuple) The piece position.
        """
        return self.__pos

    def get_typical_value(self):
        """
        Returns the typical piece value, as determined by chess conventions.
        
        :return: (float) The piece's typical value.
        """
        return self.__typical_value

    def get_char_representation(self):
        """
        Returns the typical piece notation, as determined by chess conventions.
        
        :return: (char) The piece's character representation.
        """
        return self.__char_representation


