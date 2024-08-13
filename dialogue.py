"""Contains the dialogue for the game."""

INTRO_DIALOGUE = """
***********************************************************************************
WECLOME TO PAZAAK, A STAR WARS CARD GAME! 

Pazaak is a Star Wars card game similar to Black Jack.

Players take turns drawing cards from a random deck, with the objective 
coming as close to 20 without going over.  The player with the highest score 
at the end of the round wins that round. The first player to win three rounds 
wins the match.

During each of their turns, players have the following options:
    - End their turn: a player will draw a card at the start of their next turn.
    - Play a card from their hand. A player's hand consists of four cards randomly 
        drawn from their side deck at the beginning of the match. Hand cards are 
        not replenished at the end of the round, so players have to play them carefully.
    - Stand. This ends the round for the player at their current score.

A round ends when either both players stand or one player busts. If a player 
busts, the other player automatically wins. If both players chose to stand, the 
player with the highest score at the end of the round wins.
***********************************************************************************
"""