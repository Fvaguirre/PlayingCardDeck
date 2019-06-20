class CardValidator(object):
    """Card Validator validates whether a given suit is a {"CLUBS, DIAMONDS,
    HEARTS, SPADES"} or whether a given rank is in the range 1 - 13.
    """
    def __init__(self):
        """Initializes a CardValidator object.

            Args: None.
        """
        self.__VALID_SUITS = ["CLUBS", "DIAMONDS", "HEARTS", "SPADES"]
        self.__VALID_RANKS = ["ACE"]
        for i in range(2, 11):
            self.__VALID_RANKS.append(i)
        self.__VALID_RANKS.append("JACK")
        self.__VALID_RANKS.append("QUEEN")
        self.__VALID_RANKS.append("KING")




    def isValidSuit(self, suit):
        """Checks whether a given suit is valid according to the 52 playing card
        standard (CLUBS, DIAMONDS, HEARTS, SPADES).

            Args:
                suit (str): Case-insensitive string representing card suit.

            Returns:
                (bool): Returns true if given suit is valid, false otherwise.
        """
        suit = suit.upper()
        if suit not in self.__VALID_SUITS:
            return False
        return True

    def isValidRank(self, rank):
        """Checks whether a given rank is valid according to the 52 playing card
            standard (rank can be 2-10 or ACE, JACK, QUEEN, or KING). insensitive
            to case if string.

            Args:
                rank (int) or (str): Str or Integer representing card rank.

            Returns:
                (bool): Returns true if given rank is valid, false otherwise.
        """
        if isinstance(rank, str):
            rank = rank.upper()
        if rank in self.__VALID_RANKS:
            return True
        else:
            return False
    def getValidSuits(self):
        """Gets the list of valid suits.

            Args:
                None

            Returns:
                list: Alphabetically ordered list populated with the four valid
                suits
        """
        return self.__VALID_SUITS

    def getValidRanks(self):
        """Gets the list of valid ranks.

            Args:
                None

            Returns:
                list: Numerically ordered list populated with the valid ranks.
        """
        return self.__VALID_RANKS
