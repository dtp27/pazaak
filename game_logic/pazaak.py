"""Handles the higher-level match logic and score keeping for Pazaak."""

from time import sleep
from game_logic.round import Round
from game_logic.player import Player

class Match(object):
    """Represents a Pazaak match between two players."""

    def __init__(self, player1_name, player2_name="Computer"):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)

    def show_match_score(self):
        """Displays rounds won by each plyer."""
        print("\n==========================")
        print(f"{self.player1.name} Rounds Won: {self.player1.rounds_won}")
        print(f"{self.player2.name} Rounds Won: {self.player2.rounds_won}")
        print("==========================")

    def check_winner(self):
        """Handles logic to determine winner of the match."""
        if self.player1.rounds_won == 3:
            return self.player1
        elif self.player2.rounds_won == 3:
            return self.player2
        else: 
            return None
        
    def finish_game(self, winner):
        """Handles end-game dialogue."""
        print("\n****************************\n")
        print(f"Congratulations {winner.name}, you won!!\n")
        self.show_match_score()
        print("\n****************************\n")

    def play(self):
        """Handles the match logic."""
        round_num = 0
        while not (winner := self.check_winner()):
            self.show_match_score()
            round_num += 1
            print(f"\n\nRound {round_num} starting...\n\n")
            sleep(2)

            match_round = Round()
            winner = match_round.play_round(self.player1, self.player2)
            
            # Clear the table after each round
            self.player1.cards = []
            self.player2.cards = []

            if winner:
                print(f"\n{winner.name} wins the round.\n")
            else:
                print("\nIt's a tie!\n")
            # Allow user to read before moving to next round
            sleep(2)
        
        self.finish_game(winner)
        
