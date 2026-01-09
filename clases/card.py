class Card:

    SPECIAL_CARD = {11: "JACK", 12: "QUEEN", 13: "KING", 14: "Ace"}

    def __init__(self, suit, value):
        self.value_ = value
        self.suit_ = suit

    @property
    def suit(self):
        return self.suit_
    
    @property
    def value(self):
        return self.value_
    
    def show(self):
        card_value = self.value_
        card_suit = self.suit_.description
        card_symbol = self.suit_.symbol
        if self.is_especial():
            card_description = Card.SPECIAL_CARD[self.value_]
            print(f"{card_description} of {card_suit} {card_symbol}")
        else:
            print(f"{card_value} of {card_suit} {card_symbol}")

    def is_especial(self):
        return self.value_ > 10
