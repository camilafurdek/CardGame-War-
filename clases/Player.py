class Player:
    def __init__(self, deck, is_computer = False):
        self.deck_ = deck
        self.is_computer_ = is_computer

    @property
    def is_computer(self):
        return self.is_computer
        
    @property
    def deck(self):
        return self.deck
    
    def deck_empty(self):
        return self.deck_.size == 0
    
    def draw_card(self):
        return self.deck_.draw()
    
    def add_card(self, card):
        self.deck_.add(card)

    def deck_size(self):
        return self.deck_.size

    

    
    