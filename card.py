# File: card.py
# Author: Jesse Friberg and Joonatan Silvennoinen
# Description: Card class

class Card:
    def __init__(self):
        self.price = 0
        self.id = 0
        self.owner = ""
        self.loaned = "Nobody"

    def __str__(self):
        return f"""\nCard with an ID {self.id}
Original owner: {self.owner}        
Price: {self.price} €
Currently loaned by: {self.loaned}"""

    def show_card(self):
        print(self)

    def set_price(self, price):
        self.price = price

    def set_id(self, id):
        self.id = id

    def set_owner(self, own):
        self.owner = own

    #Loaner will be self.name of the player who loans the card as the argument in the main function 
    def set_loaned_yes(self, loaner):
        self.loaned = loaner

    def set_loaned_no(self):
        self.loaned = "Nobody"

    def get_price(self):
        return self.price
    
    def get_id(self):
        return self.id

    def get_owner(self):
        return self.owner

    def get_loaned(self):
        return self.loaned


def main():

    kortti = Card()
    kortti.set_price(15)
    kortti.set_owner("Jesse")
    kortti.set_loaned_yes("Joonatan")

    print(kortti)

