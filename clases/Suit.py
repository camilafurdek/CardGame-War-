class Suit:
    SYMBOLS = {"Clubs": "♣", "Dimonds": "♦", "Hearts": "♥", "Spades": "♠"}
    def __init__(self, description):
        self.description_ = description
        self.symbol_ = Suit.SYMBOLS[description]

    @property 
    def description(self):
        return self.description_
    
    @property
    def symbol(self):
        return self.symbol_