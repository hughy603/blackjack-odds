""" Represents a deck of cards
"""
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class Deck(collections.MutableSequence):
    """ One or many decks of cards
    """
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self, size=1):
        self._cards = size * [Card(rank, suit) for suit in self.suits
                              for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, position, value):
        self._cards[position] = value

    def __delitem__(self, position):
        del self._cards[position]

    def insert(self, position, value):
        self._cards.insert(position, value)
