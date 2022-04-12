# File: main.py
# Author: Jesse Friberg and Joonatan Silvennoinen
# Description: main file for the program that allows you to keep track of your trading cards

from card import Card, Mtg_card, Pokemon_card, Yugioh_card
from player import Player

def player_create():
    global player_dic
    while True:
        name = input("Enter your username: ").capitalize()
        if name in  player_dic:
            print("That username already exists, please choose another one!")
        else:
            break
    player_dic[name] = Player()  
    player_dic[name].set_name(name)
    
    

def basic_card_create(card, name):
    card_name = input("\nEnter the name of the card: ").capitalize()
    while True:
        price = input("Enter the price of the card as an integer: ")
        try:
            price = int(price)
            break
        except ValueError:
            print("Please enter a valid integer")
            continue
    card.set_price(price)
    card.set_name(card_name)
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
    
    color = input("Enter the color of the card (Red, Blue, Green, Black, White or Colorless, or any combination of them): ").capitalize()
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
    
    return card

def pokemon_card_create(empty_card, name):
    card = basic_card_create(empty_card, name)
    type_list = ["Pokémon", "Energy", "Trainer"]
    print("Select the number correspoding the correct card type")
    print("Pokémon   Energy     Trainer")
    print("  1          2          3")
    while True:
        answ = input()
        try:
            answ = int(answ)
            if answ not in [1,2,3]:
                print("Please enter a valid answer")
                continue
            else:
                break
        except:
            print("Please enter a valid number")
            continue

    card.set_card_type(type_list[answ-1])

    typing_list = ["Grass", "Fire", "Water", "Lightning", "Fighting", 
    "Psychic", "Colorless", "Darkness", "Metal", "Dragon", "Fairy"]
    print("Select the number correspoding the correct typing for the card")
    print("Grass    Fire    Water    Lightning    Fighting    Psychic    Colorless    Darkness    Metal    Dragon    Fairy")
    print("  1       2        3          4            5          6           7           8          9        10        11")
    while True:
        answ = input()
        try:
            answ = int(answ)
            if answ not in [1,2,3,4,5,6,7,8,9,10,11]:
                print("Please enter a valid answer")
                continue
            else:
                break
        except:
            print("Please enter a valid number")
            continue

    card.set_typing(typing_list[answ-1])

    if card.get_card_type() == "Pokémon":
        while True:
            hp = input("Enter the pokémons hp as an integer: ")
            try:
                hp = int(hp)
                break
            except ValueError:
                print("Please enter a valid integer")
                continue
        card.set_hp(hp)
    else:
        card.set_hp("None")

    return card
        
def yugioh_card_create(empty_card, name):
    card = basic_card_create(empty_card, name)
    type_list = ["Monster", "Spell", "Trap"]
    print("Select the number correspoding the correct card type")
    print("Monster   Spell   Trap")
    print("  1         2       3")
    while True:
        answ = input()
        try:
            answ = int(answ)
            if answ not in [1,2,3]:
                print("Please enter a valid answer")
                continue
            else:
                break
        except:
            print("Please enter a valid number")
            continue

    card.set_type(type_list[answ-1])

    rarity_list = ["Common", "Rare", "Super Rare", "Holofoil Rare", "Ultra Rare",
    "Ultimate Rare", "Secret Rare", "Parallel Rare", "Ghost Rare", "Gold Ultra Rare"]
    print("Select the number correspoding the correct typing for the card")
    print("Common  Rare  Super Rare  Holofoil Rare  Ultra Rare   Ultimate Rare  Secret Rare  Parallel Rare  Ghost Rare  Gold Ultra Rare")
    print("  1       2       3             4            5              6             7              8           9              10")
    while True:
        answ = input()
        try:
            answ = int(answ)
            if answ not in [1,2,3,4,5,6,7,8,9,10]:
                print("Please enter a valid answer")
                continue
            else:
                break
        except:
            print("Please enter a valid number")
            continue

    card.set_rarity(rarity_list[answ-1])

    while True:
        grade = input("Enter the grade of the card from 1 to 10 as an integer: ")
        try:
            grade = int(grade)
            if grade not in [1,2,3,4,5,6,7,8,9,10]:
                print("Please enter a valid grade")
                continue
            else:
                card.set_grade(grade)
                break
        except ValueError:
            continue

    return card

player_dic = {}
latest_id = 0

def int_check(num):
    while True:
        try:
            num = int(num)
            return num
        except ValueError:
            print("Please enter a valid number:")
            num = input()
            continue

def player_choose():
    for count, player in enumerate(player_dic.keys()):
        print(f"{count+1}. {player}")
    keys = list(player_dic.keys())   
    while True:
        answ = input("Choose a player: ")
        answ = int_check(answ)
        if answ <= count+1:
            return player_dic[keys[answ-1]].get_name()
        else:
            print("Please enter an available option")
            continue 
        
def main_menu(user):
    print(f"\nGreetings {user}, what would you like to do?")
    print("1. Add or remove a card")
    print("2. Loan a card or add a card up for loaning")
    print("3. View collections")
    print("4. Quit")
    while True:
        answ = input()
        answ = int_check(answ)
        if answ in [1,2,3,4]:
            if answ == 1:
                #add a card
                add_card(user)
                break
            elif answ == 2:
                #loan a card
                break
            elif answ == 3:
                #view all card collections
                view_collections(user)
                break
            elif answ == 4:
                #Quit button
                print("Goodbye!")
                exit()
        else:
            print("Please enter an available option")
            continue
    
def add_card(user):
    print("\nWhat kind of card would you like to add?")
    print("1. Magic The Gathering")
    print("2. Pokémon")
    print("3. Yu-Gi-Oh")
    while True:
        answ = input()
        answ = int_check(answ)
        if answ in [1,2,3]:
            if answ == 1:
                #create mtg card
                card = Mtg_card()
                card = mtg_card_create(card, user)
                break
            elif answ == 2:
                #create pokemon card
                card = Pokemon_card()
                card = pokemon_card_create(card, user)
                break
            elif answ == 3:
                #create yugioh card
                card = Yugioh_card()
                card = yugioh_card_create(card, user)
                break
        else:
            print("Please enter an available option")
            continue
    
    #Add the created card to the user and print it out
    player_dic[user].add_card_owned(card)
    print(player_dic[user].get_owned_cards()[len(player_dic[user].get_owned_cards())-1])
    
    print("\nWould you like to add another card?")
    print("1. Yes, add another card")
    print("2. No, return to main menu")
    print("3. Quit")
    while True:
        answ = input()
        answ = int_check(answ)
        if answ in [1,2,3]:
            if answ == 1:
                add_card(user)
                break
            elif answ == 2:
                main_menu(user)
                break
            elif answ == 3:
                #Quit button
                print("Goodbye!")
                exit()
        else:
            print("Please enter an available option")
            continue
        
def view_collections(current_user):
    print("\nWhich player's collection would you like to view?")
    chosen_player = player_choose()
    
    print(f"\n{chosen_player}'s card collection: ")
    for i in player_dic[chosen_player].get_owned_cards():
        print(i)
        
    print("\nWould you like to view another player's collection?")
    print("1. Yes, view another collection")
    print("2. No, return to main menu")
    print("3. Quit")
    while True:
        answ = input()
        answ = int_check(answ)
        if answ in [1,2,3]:
            if answ == 1:
                view_collections()
                break
            elif answ == 2:
                main_menu(current_user)
                break
            elif answ == 3:
                #Quit button
                print("Goodbye!")
                exit()
        else:
            print("Please enter an available option")
            continue

            
def main():
    #On startup
    print("Greetings")
    # * placeholder for instructions later on * 
    print("Do you want to create a new player or choose an existing one?")
    print("1. New player")
    print("2. Existing player")
    print("3. Quit")
    while True:
        answ = input()
        answ = int_check(answ)
        if answ in [1,2,3]:
            if answ == 1:
                player_create()
                break
            elif answ == 2:
                if len(player_dic) == 0:
                    print("No existing players, choose another option: ")
                    continue
                else:
                    break
            elif answ == 3:
                exit()
        else:
            print("Please enter an available option")
            continue
    
    #User gets to choose which registered player they want to use 
    current_player = player_choose()
    
    #The main menu loop where player can navigate everywhere
    main_menu(current_player)
    
    

    

main()

    

                













