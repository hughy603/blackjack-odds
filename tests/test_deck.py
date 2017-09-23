from cards.deck import Deck

SUITS = 4
RANKS = 13
CARDS = SUITS * RANKS

def test_deck_count():
    assert len(Deck()) == CARDS

def test_multi_deck_count():
    assert len(Deck(size=3)) == CARDS * 3

def test_deck_suits():
    assert len(Deck.suits) == SUITS

def test_deck_ranks():
    assert len(Deck.ranks) == RANKS