"""Handles the card objects for Pazaak."""

from random import randint


class Card(object):
    """Represents a signle Pazaak card."""

    def __init__(self, value):
        self.value = value

class Deck(object):
    """Represents a full Pazaak deck for a round."""

    def __init__(self):
        # a deck consists of 4 of each card 1 - 10
        self.cards = []
        for i in range(1,11):
            self.cards.extend([Card(i), Card(i), Card(i), Card(i)])
        
    def draw_card(self):
        """Draws a single card from the deck at random."""
        random_draw_index = randint(0, len(self.cards)-1)
        return self.cards.pop(random_draw_index)

class SideDeck(object):
    """Represents a player's side deck that the hand is chosen from."""

    def __init__(self, extra_cards):
        self.cards = []
        # by default, players have 2 of each cards 1 - 5 in their side deck
        for i in range(1,6):
            self.cards.extend([Card(i), Card(i)])
        # players have the option to add more cards if they have them
        self.cards.extend(extra_cards)
