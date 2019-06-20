
class Card(object):
    """Card is a single playing card with integer ranks, and string suit.
    """
    def __init__(self, suit, rank):
        """Instantiates Card object instance to given suit and rank.

            Args:
                suit (str): Case-insensitive string representation of suit.

                rank (int): Representation of card rank.

        """
        self.__suit = suit

        self.__rank = rank

    def __str__(self):
        """Returns string representation of card. Example: 'Suit: Hearts'; Rank:
        2'.
        """
        return "Suit: " + self.__suit + "; Rank: " + str(self.__rank) + "\n"

    def __eq__(self, other):
        """Returns true if both rank and suit match (suit is case-insensitive);
            however, rank must match exactly.
        """

        if (other.getRank() == self.__rank) and (other.getSuit().lower() == self.__suit.lower()):
            return True
        else:
            return False

    def __ne__(self, other):
        """Returns false if either rank or suit don't match."""
        return not self.__eq__(other)

    def getRank(self):
        """Getter for card instance's given rank.

            Args:
                None.

            Returns:
                int: The card's rank.
        """
        return self.__rank

    def getSuit(self):
            """Getter for card instance's given suit.

                Args:
                    None.

                Returns:
                    str: The card's given suit.
            """
            return self.__suit
