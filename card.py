# File: card.py
# Author: Jesse Friberg and Joonatan Silvennoinen
# Description: Card class and its subclasses

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


class Mtg_card(Card):

    def __init__(self):
        self.type = ""
        self.color = ""
        self.comp_legality = ""
        Card.__init__(self)

    def __str__(self):
        return f"""\nMagic the Gathering card with an ID {self.id}
Original owner: {self.owner}        
Price: {self.price} €
Card type: {self.type}
Card color: {self.color}
Is the card tournament legal: {self.comp_legality}
Currently loaned by: {self.loaned}"""

    def set_type(self, type):
        self.type = type

    def set_color(self, color):
        self.color = color

    def set_legality_yes(self):
        self.comp_legality = "Yes"

    def set_legality_no(self):
        self.comp_legality = "No"

    def get_type(self):
        return self.type

    def get_color(self):
        return self.color

    def get_legality(self):
        return self.comp_legality


class Pokemon_card(Card):

    def __init__(self):
        self.card_type = ""
        self.typing = ""
        self.hp = 0
        Card.__init__(self)

    def __str__(self):
        return f"""\nPokémon card with an ID {self.id}
Original owner: {self.owner}        
Price: {self.price} €
Card type: {self.card_type} card
Card typing: {self.typing}
HP of the card: {self.hp}
Currently loaned by: {self.loaned}"""

    def set_card_type(self, type):
        self.card_type = type

    def set_typing(self, typing):
        self.typing = typing

    def set_hp(self, hp):
        self.hp = hp

    def get_card_type(self):
        return self.card_type

    def get_typing(self):
        return self.typing

    def get_hp(self):
        return self.hp


class Yugioh_card(Card):

    def __init__(self):
        self.type = ""
        self.rarity = ""
        self.grade = 0
        Card.__init__(self)

    def __str__(self):
        return f"""\nYu-Gi-Oh card with an ID {self.id}
Original owner: {self.owner}        
Price: {self.price} €
Card type: {self.type}
Card rarity: {self.rarity}
Card grade: {self.grade}
Currently loaned by: {self.loaned}"""

    def set_type(self, type):
        self.type = type

    def set_rarity(self, rarity):
        self.rarity = rarity

    def set_grade(self, grade):
        self.grade = grade

    def get_type(self):
        return self.type

    def get_rarity(self):
        return self.rarity

    def get_grade(self):
        return self.grade
