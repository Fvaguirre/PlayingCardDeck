import random
from Card import Card
from CardValidator import CardValidator

class Deck(object):
    """Deck is a representation of the standard 52 playing card deck."""
    def __init__(self):
        """Creates an ordered (Suits in alphabetical order, and ranks in
        numerical order) standard 52 playing card deck.

            Args:
                None.
        """
        self.__validator = CardValidator()
        self.__deck = []
        for suit in self.__validator.getValidSuits():
            for rank in self.__validator.getValidRanks():
                self.__deck.append(Card(suit, rank))

    def getLength(self):
        """Returns the number of cards left in the deck.

            Args:
                None.

            Returns:
                int: Integer number of cards left in deck.
        """
        return len(self.__deck)

    def dealCard(self):
        """Deals a card from the top of the deck.

            Args:
                None.

            Returns:
                Card : The card at the top of the deck if the deck is not empty,
                otherwise it returns None.

            Modifies:
                The current card at the top of the deck.
        """
        if len(self.__deck) > 0:
            current_card = self.__deck.pop(0)
            return current_card
        else:
            return None


    def shuffle(self):
        """Randomly shuffles the deck.

            Args:
                None.

            Returns:
                None.

            Modifies:
                The order of the cards within the deck.
        """
        # Courtesy of Mr. Fisher and Mr. Yates ;)
        for i in range(len(self.__deck) - 1, 0, -1):
            rand_index = random.randint(0, i)
            # Swap current index with rand_index card
            temp = self.__deck[i]
            self.__deck[i] = self.__deck[rand_index]
            self.__deck[rand_index] = temp
