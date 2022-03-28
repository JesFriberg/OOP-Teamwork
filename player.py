# File: player.py
# Author: Jesse Friberg and Joonatan Silvennoinen
# Description: player class

class Player():

    def __init__(self):
        self.name = ""
        self.owned_cards = []
        self.cards_for_trade = []
        self.loaned_cards = {}
        
    def __str__(self):
        return f"""\nData of {self.name}
Owned cards: {self.owned_cards}
Loaned cards: {self.loaned_cards}  
Cards {self.name} has put up for trading: {self.cards_for_trade}  """

    def set_name(self, name):
        self.name = name

    def add_card_owned(self, card):
        self.owned_cards.append(card)

    def add_card_for_trade(self, card):
        self.cards_for_trade.append(card)

    def add_card_loaned(self, owner, card):
        self.loaned_cards[f"Original owner: {owner}"] = card

    def get_name(self):
        return self.name

    def get_owned_cards(self):
        return self.owned_cards

    def get_cards_for_trade(self):
        return self.cards_for_trade

    def get_loaned_cards(self):
        return self.loaned_cards


def main():
    
    jesse = Player()
    jesse.set_name("Jesse")
    jesse.add_card_owned("Holo charizard")
    jesse.add_card_owned("Pikachu")
    jesse.add_card_loaned("Joonatan", "Full art Krenko")
    owned = jesse.get_owned_cards()
    jesse.add_card_for_trade(owned[1])

    print(jesse)


main()