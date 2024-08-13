"""Implements a Pazaak game with high-level user options."""

from game_logic.pazaak import Match
from dialogue import INTRO_DIALOGUE


def get_player_name(player_num):
    """Handles the logic to ensure each player has a proper, unique name."""
    while True:
        player_name = input(f"\nPlayer {player_num}, enter your name: ")
        if player_name == "":
            print("You must have a name.")
        elif player_name in player_names:
            print("Each player name must be unique.")
        else:
            player_names.append(player_name)
            return player_name

print(INTRO_DIALOGUE)
input("Press Enter to continue...\n")

player_names = []
player1_name = get_player_name(1)
player2_name = get_player_name(2)

match = Match(player1_name, player2_name)
match.play()