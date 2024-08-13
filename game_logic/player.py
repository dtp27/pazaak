"""Handles the Pazzak player logic."""

from random import randint
from game_logic.cards import SideDeck


class Hand(object):
    """Represents a player's hand in a Pazaak match."""

    def __init__(self, side_deck):
        # Draw four random cards from the side deck to have as hand cards
        self.cards = []
        for i in range(0,4):
            random_draw_index = randint(0, len(side_deck.cards)-1)
            hand_card = side_deck.cards.pop(random_draw_index)
            self.cards.append(hand_card)
    
    def remove_card(self, card):
        """Handles removing a card from the player's hand."""
        self.cards.remove(card)
        

class Player(object):
    """Represents a Pazaak player."""

    def __init__(self, name, side_deck = []):
        self.name = name
        self.side_deck = SideDeck(side_deck)
        self.hand = Hand(self.side_deck)
        self.rounds_won = 0
        self.cards = []
        self.round_ended = False

    def add_card(self, card):
        """Handles adding a card to the table for the player."""
        self.cards.append(card)

    def get_score(self):
        """Gets the current sum of card values on the table for that player."""
        score = 0
        for card in self.cards:
            score += card.value
        return score

 
    def show_table(self):
        """Shows player's side of the Pazaak table."""
        print("---------------------------")
        print("Active Cards:", end=' ')
        for card in self.cards:
            print(card.value, end=' ')
        print("\nActive Card Total:", self.get_score())
        print("Cards in Hand:", end=' ')
        for card in self.hand.cards:
            print(card.value, end=' ')
        print("\n---------------------------")

    def play_card(self):
        """Handles logic for when a card is played from the player's hand."""
        card_choice = ""

        hand_choices = [card.value for card in self.hand.cards]
        while card_choice not in hand_choices:
            try:
                print("\nEnter the hand card you wish to play.")
                card_choice = int(input("> "))
                if card_choice not in hand_choices:
                    print("You don't have that card in your hand.") 
            except:
                print("Enter a valid card value.")

        # remove the card from the hand
        # need to stop after first occurance to avoid removing more than one card
        for card in self.hand.cards:
            if card.value == card_choice:
                self.hand.remove_card(card)
                break
                
        return int(card_choice)
    
    def reset(self):
        """Handles resetting player settings after each round."""
        self.cards = []
        self.round_ended = False
