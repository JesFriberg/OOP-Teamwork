# File: main.py
# Author: Jesse Friberg and Joonatan Silvennoinen
# Description: main file for the program that allows you to keep track of your trading cards

from card import Card, Mtg_card, Pokemon_card, Yugioh_card
from player import Player



def basic_card_create(card, name):
    while True:
        price = input("Enter the price of the card as an integer: ")
        try:
            price = int(price)
            break
        except ValueError:
            print("Please enter a valid integer")
            continue
    card.set_price(price)
    
    global latest_id
    card.set_id(latest_id+1)
    latest_id +=1

    card.set_owner(name)
    
    return card


def mtg_card_create(empty_card, name):
    card = basic_card_create(empty_card, name)
    type_list = ["Land", "Creature", "Artifact", "Enchantment", "Planeswalker", "Insant", "Sorcery"]
    print("Select the number correspoding the correct card type")
    print("Land  Creature  Artifact  Enchantment  Planeswalker  Instant  Sorcery")
    print(" 1       2         3           4            5           6         7 ")
    while True:
        answ = input()
        try:
            answ = int(answ)
            if answ not in [1,2,3,4,5,6,7]:
                print("Please enter a valid answer")
                continue
            else:
                break
        except:
            print("Please enter a valid number")
            continue

    card.set_type(type_list[answ-1])
    
    color = input("Enter the color of the card (Red, Blue, Green, Black, White or Colorless, or any combination of them): ")
    card.set_color(color)

    while True:
        legal = input("Is this card tournament legal: ").capitalize()
        if legal not in ["Yes", "No"]:
            print("Please enter yes or no")
            continue
        else:
            if legal == "Yes":
                card.set_legality_yes()
            elif legal == "No":
                card.set_legality_no()
            break
    
    print(card)
    
latest_id = 0 
kortti = Mtg_card()
mtg_card_create(kortti, "Jesse")




