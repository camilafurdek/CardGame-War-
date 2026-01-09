class WarCardGame:
    PLAYER = 0
    COMPUTER = 1
    TIE = 2
    
    def __init__(self, player, computer, deck):
        self.player_ = player
        self.computer_ = computer
        self.deck_ = deck

        self.make_initial_deck()

    def make_initial_deck(self):
        self.deck_.shuffle()
        self.make_deck(self.player_)
        self.make_deck(self.computer_)

    def make_deck(self, player):
        for i in range(26):
            card = self.deck_.draw()
            player.add_card(card)

    def start_battle(self, cards_from_war = None):
        if not (self.player_.deck_empty() or self.computer_.deck_empty()):
            print("\n== Start the battle ==\n")
            player_card = self.player_.draw_card()
            computer_card = self.computer_.draw_card()
            print("Your card:\n")
            player_card.show()
            print(f"\nComputer card:\n")
            computer_card.show()
            print("\n")
            winner = self.get_round_winner(player_card, computer_card)
            cards_won = self.get_cards_won(player_card, computer_card, cards_from_war)
            if winner == WarCardGame.PLAYER:
                print("You won this round\n")
                self.add_cards_to_player(self.player_,cards_won)
            elif winner == WarCardGame.COMPUTER:
                print("Ypu lost this round\n")
                self.add_cards_to_player(self.computer_,cards_won)
            else:
                print("There is a tie, this is war!")
                self.start_war(cards_won)
            return winner
    
    def get_round_winner(self, player_card, computer_card):
        if player_card.value > computer_card.value:
            return WarCardGame.PLAYER
        elif player_card.value < computer_card.value:
            return WarCardGame.COMPUTER
        else:
            return WarCardGame.TIE
        
    def get_cards_won(self, player_card, computer_card, cards_from_war):
        if cards_from_war:
            return [player_card, computer_card] + cards_from_war
        else:
            return [player_card, computer_card]
        
    def add_cards_to_player(self, player, cards_won):
        for card in cards_won:
            player.add_card(card)

    def start_war(self, cards_won = None):
        if (self.player_.deck_size() > 2 and self.computer_.deck_size()):
            player_cards = []
            computer_cards = []
            for i in range(3):
                player_cards.append(self.player_.draw_card())
                computer_cards.append(self.computer_.draw_card())
            print("Six hidden cards\n")
            if cards_won:
                self.start_battle(player_cards + computer_cards + cards_won)
            else:
                self.start_battle(player_cards + computer_cards)
        elif self.player_.deck_size() < 3:
            self.player_.deck_.clear_deck()
        else:
            self.computer.deck_.clear_deck()

    def game_over(self):
        if self.player_.deck_empty():
            print("=============================\n")
            print("|         GAME OVER         |")
            print("=============================\n")
            print("Try again, the computer won.")
            return True
        elif self.computer_.deck_empty():
            print("=============================\n")
            print("|         GAME OVER         |")
            print("=============================\n")
            print("YOU WON !!.")
            return True
        else:
            return False
        
    def stats(self):
        print(f"\n----")
        print(f"\n You have: {self.player_.deck_.size} cards")
        print(f"\n The computer has: {self.computer_.deck_.size} cards")
        print(f"\n----")

    def welcome_message(self):
        print("=============================\n")
        print("|       WAR CARD GAME       |\n")
        print("=============================\n")
