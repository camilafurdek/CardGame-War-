import random

from .card import Card
from .Suit import Suit


class Deck:
    SUITS = {"Clubs", "Dimonds", "Hearts", "Spades"}

    def __init__(self, is_empty = False):
        self.cards_ = []
        if not is_empty:
            self.create()

    @property
    def size(self):
        return len(self.cards_)
    
    def create(self):
        for suit_ in Deck.SUITS:
            for value_ in range(2,15):
                self.cards_.append(Card(Suit(suit_), value_))

    def show(self):
        for card in self.cards_:
            card.show()
    
    def shuffle(self):
        random.shuffle(self.cards_)

    def draw(self):
        if self.cards_:
            return self.cards_.pop()
        return None
    
    def add(self, card):
        self.cards_.insert(0, card)

    def clear_deck(self):
        self.cards_.clear()