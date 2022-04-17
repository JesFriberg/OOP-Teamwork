# File: main.py
# Author: Jesse Friberg and Joonatan Silvennoinen
# Description: main file for the program that allows you to keep track of your trading cards

from card import Card, Mtg_card, Pokemon_card, Yugioh_card
from player import Player
import pickle

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
    #The main hub where user can access all the features
    while True:
        print(f"\nGreetings {user}, what would you like to do?")
        print("1. Add or remove a card")
        print("2. Loan a card or add a card up for loaning")
        print("3. View collections")
        print("4. Change player")
        print("5. Quit")
        while True:
            answ = input()
            answ = int_check(answ)
            if answ in [1,2,3,4,5]:
                if answ == 1:
                    #add a card
                    add_card(user)
                    break
                elif answ == 2:
                    #loan a card
                    loan_card(user)
                    break
                elif answ == 3:
                    #view all card collections
                    view_collections()
                    break
                elif answ == 4:
                    #returns back to the beginning, allowing the change or creation  of players
                    return
                elif answ == 5:
                    #Quit button
                    pickle_out = open("dict.pickle","wb")
                    pickle.dump(player_dic, pickle_out)
                    pickle_out.close()
                    print("Goodbye!")
                    exit()
            else:
                print("Please enter an available option")
                continue
    
def add_card(user):
    global player_dic
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
    
    #Add the created card to the user 
    player_dic[user].add_card_owned(card)
    

    #Ask the user if the card is up for loaning
    while True:
        legal = input("\nDo you want to put this card up for loaning?: ").capitalize()
        if legal not in ["Yes", "No"]:
            print("Please enter yes or no")
            continue
        else:
            if legal == "Yes":
                card.set_up_for_loan("Yes")
                player_dic[user].add_card_for_loan(card)
            break

    #Print the added card out
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
                pickle_out = open("dict.pickle","wb")
                pickle.dump(player_dic, pickle_out)
                pickle_out.close()
                add_card(user)
                break
            elif answ == 2:
                pickle_out = open("dict.pickle","wb")
                pickle.dump(player_dic, pickle_out)
                pickle_out.close()
                return
                
            elif answ == 3:
                #Quit button
                pickle_out = open("dict.pickle","wb")
                pickle.dump(player_dic, pickle_out)
                pickle_out.close()
                print("Goodbye!")
                exit()
        else:
            print("Please enter an available option")
            continue
        
def view_collections():
    #Choose a player and print out each card in that players owned_cards list
    print("\nWhich player's collection would you like to view?")
    chosen_player = player_choose()
    if len(player_dic[chosen_player].get_owned_cards()) > 0 or len(player_dic[chosen_player].get_loaned_cards()) > 0:
        print(f"\n{chosen_player}'s card collection: ")
        if len(player_dic[chosen_player].get_owned_cards()) == 0:
            print(f"\n{chosen_player} does not currently own any cards")
        for i in player_dic[chosen_player].get_owned_cards():
            print(i)

        print(f"\n{chosen_player}'s loaned cards: ")
        if len(player_dic[chosen_player].get_loaned_cards()) == 0:
            print(f"\n{chosen_player} does not currently have any loaned cards")
        for i in player_dic[chosen_player].get_loaned_cards():
            print(i)      
    else:
        print(f"\n{chosen_player}'s card collection is empty at the moment.")
        
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
                return
            elif answ == 3:
                #Quit button
                print("Goodbye!")
                exit()
        else:
            print("Please enter an available option")
            continue

def loan_card(current_user):  
    global player_dic
    all_cards_for_loan = []  
    counter = []   
    #Go trough every players loanable cards list and add them into one single list
    for i in player_dic:
        if player_dic[i].get_name() == current_user:
            continue
        else:
            for i in player_dic[i].get_cards_for_loan():
                all_cards_for_loan.append(i)   
    
    if len(all_cards_for_loan) > 0:
        print("\nHere are all the cards other players have put up able to be loaned: ")
    else: 
        print("\nThere is no cards up for loaning at the moment.")
        print("Returning to main menu...")
        return

    for count, card in enumerate(all_cards_for_loan):
        print(f"\nLoan ID: {count+1} {card}")
        counter.append(count+1)

    print("\nWhich card would you like to loan?")
    print("Enter the Loan ID of the desired card or type 0 to return to main menu: ")
    while True:
        answ = input()
        answ = int_check(answ)
        if answ in counter:
            #Addes the card to current users loaned cards, removes the card from loanable cards
            print(f"Adding {all_cards_for_loan[answ-1].get_name()} to your collection...")
            all_cards_for_loan[answ-1].set_loaned_yes(current_user)
            player_dic[current_user].add_card_loaned(all_cards_for_loan[answ-1])
            player_dic[all_cards_for_loan[answ-1].get_owner()].get_cards_for_loan().pop(answ-1)
            pickle_out = open("dict.pickle","wb")
            pickle.dump(player_dic, pickle_out)
            pickle_out.close()
            break
        elif answ == 0:
            #returns to main menu
            pickle_out = open("dict.pickle","wb")
            pickle.dump(player_dic, pickle_out)
            pickle_out.close()
            return 
        else:
            print("Please choose a valid option")
            continue


def main():
    while True:
        global player_dic
        #Checks if there is a saved state
        while True:
            try:
                pickle_in = open("dict.pickle", "rb")
                player_dic = pickle.load(pickle_in)
                if len(player_dic) == 0:
                    print("No save file found!")
                    break
                else:
                    print("Save file found!")
                    break
            except FileNotFoundError:
                print("No save file found")
                break
        print("\nGreetings")
        print("You can navigate around by typing the number corresponding the option you want to choose!")
        print("Do you want to create a new player or choose an existing one?")
        print("1. New player")
        print("2. Existing player")
        print("3. Clear current save file")
        print("4. Quit")
        while True:
            answ = input()
            answ = int_check(answ)
            if answ in [1,2,3,4]:
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
                    print("Are you sure you want to clear the save file?")
                    while True:
                        clear = input().capitalize()
                        if clear not in ["Yes", "No"]:
                            print("Please enter yes or no")
                            continue
                        else:
                            if clear == "Yes":
                                empty_list = {}
                                pickle_out = open("dict.pickle","wb")
                                pickle.dump(empty_list, pickle_out)
                                pickle_out.close()
                                print("The programm needs to be restarted after clearing the save file")
                                exit()
                            elif clear == "No":
                                print("The save file was not cleared")
                                break  
                    print("Do you want to create a new player or choose an existing one?")
                    print("1. New player")
                    print("2. Existing player")
                    print("3. Clear current save file")
                    print("4. Quit")                 
                    continue
                elif answ == 4:
                    pickle_out = open("dict.pickle","wb")
                    pickle.dump(player_dic, pickle_out)
                    pickle_out.close()
                    exit()
            else:
                print("Please enter an available option")
                continue
        
        pickle_out = open("dict.pickle","wb")
        pickle.dump(player_dic, pickle_out)
        pickle_out.close()

        #User gets to choose which registered player they want to use 
        current_player = player_choose()
        
        #The main menu loop where player can navigate everywhere
        main_menu(current_player)
    
player_dic = {}
latest_id = 0
main()

    
