# File: player.py
# Author: Jesse Friberg and Joonatan Silvennoinen
# Description: player class

class Player():

    def __init__(self):
        self.name = ""
        self.owned_cards = []
        self.cards_for_loan = []
        self.loaned_cards = []
        
    def __str__(self):
        return f"""\nData of {self.name}
Owned cards: {self.owned_cards}
Loaned cards: {self.loaned_cards}  
Cards {self.name} has put up for loan: {self.cards_for_loan}  """

    def set_name(self, name):
        self.name = name

    def add_card_owned(self, card):
        self.owned_cards.append(card)

    def add_card_for_loan(self, card):
        self.cards_for_loan.append(card)

    def add_card_loaned(self, card):
        self.loaned_cards.append(card)

    def get_name(self):
        return self.name

    def get_owned_cards(self):
        return self.owned_cards

    def get_cards_for_loan(self):
        return self.cards_for_loan

    def get_loaned_cards(self):
        return self.loaned_cards


