""" Entry point into the blackjack calculation program
"""
import sys
from cards.deck import Deck

def main():
    deck = Deck(2)
    print(len(deck), 'cards')

if __name__ == '__main__':
    sys.exit(main())
