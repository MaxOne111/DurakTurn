from enum import Enum

class ECardRank(Enum):
    SIX = 1
    SEVEN = 2
    EIGHT = 3
    NINE = 4
    TEN = 5
    JACK = 6
    QUEEN = 7
    KING = 8
    ACE = 9


class ECardSuits(Enum):
    SPADE = '♥'
    DIAMOND = '♦'
    HEART = '♣'
    CLUB = '♠'

class Card:
    suit: ECardSuits
    rank: ECardRank

    def __init__(self, suit: ECardSuits, rank: ECardRank):
        self.suit = suit
        self.rank = rank



