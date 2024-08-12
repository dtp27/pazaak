"""Implements a Pazaak game with high-level user options."""

from game_logic.pazaak import Match
from dialogue import INTRO_DIALOGUE


print(INTRO_DIALOGUE)
input("Press any key to continue...\n")

player1_name = input("Player 1, enter your name: ")
player2_name = input("Player 2, enter your name: ")

match = Match(player1_name, player2_name)
match.play()