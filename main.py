from clases.Player import Player
from clases.Deck import Deck
from clases.war_card_game import WarCardGame

player = Player(Deck(is_empty = True))
computer = Player(Deck(is_empty = True), is_computer = True)

deck = Deck()

game = WarCardGame(player, computer, deck)

game.welcome_message()

while not game.game_over():
    game.start_battle()
    game.stats()
    answer = input("Are you ready to start a new round?, press enter to continue\n Press x to stop the game ")
    if answer.lower() == "x":
        break

