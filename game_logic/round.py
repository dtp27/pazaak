"""Handles the logic for the individual Pazzak rounds."""

from game_logic.cards import Card, Deck


class Round(object):
    """Represents a round of Pazaak."""
    
    def __init__(self):
        self.deck = Deck()
    
    def play_turn(self, player):
        """Handles all logic for a single turn for a player."""
        # Player always starts the turn drawing a card
        card = self.deck.draw_card()
        player.add_card(card)
        print("\nTurn:", player.name)
        player.show_table()
        # Can only play one hand card per turn, so it needs to be tracked
        hand_played = False

        # Allows player to make certain moves during the turn
        while player.get_score() < 20:
            print(player.name, ", please choose a move {end turn (E) | play hand (H) | stand (S)}")
            turn_choice = input("> ")

            # convert short hand to full choice for clarity
            if turn_choice.upper() == "E":
                turn_choice = "end turn"
            elif turn_choice.upper() == "H":
                turn_choice = "play hand"
            elif turn_choice.upper() == "S":
                turn_choice = "stand"

            # can only play hand once per turn
            # and must be one of the four cards in the player's hand
            if turn_choice == "play hand":
                if not hand_played:
                    card_value = player.play_card()
                    player.add_card(Card(card_value))
                    player.show_table()
                    hand_played = True
                else:
                    print("Only one hand card per turn can be played.")
            elif turn_choice in ["end turn", "stand"]: 
                break
            else:
                print("That's not a valid choice.")

        # player will automatically stand if they hit or go over 20
        try:
            if player.get_score() >= 20:
                return "stand"
            else:
                return turn_choice
        except:
            return "stand"

    def get_winner(self, player1, player2):
        """Determines which player won the round."""
        # Evaluate and return who won the round
        if player1.get_score() > 20:
            player2.rounds_won += 1
            return player2
        elif player2.get_score() > 20:
            player1.rounds_won += 1
            return player1
        elif player2.get_score() > player1.get_score():
            player2.rounds_won += 1
            return player2
        elif player1.get_score() > player2.get_score():
            player1.rounds_won += 1
            return player1
        else:
            return None

    def play_round(self, player1, player2):
        """Handles all logic for a single round for the players."""
        turn_choice = "end turn"
        while not (player1.round_ended and player2.round_ended):
            
            for player in [player1, player2]:
                # player can play as long as their turn
                if not player.round_ended:
                    turn_choice = self.play_turn(player)
                    if turn_choice == "stand":
                        player.round_ended = True
                        # if one player busts, the round ends
                        if player.get_score() > 20:
                            return self.get_winner(player1, player2)
                        
        return self.get_winner(player1, player2)
