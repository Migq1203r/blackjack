import os
import random
cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]

dowantplay = input("Do you want play blackjack? [Y/n]: ")

first_time = True
cards_people_perm = []
cards_computer_perm = []
def start():
    global first_time
    global cards_people_perm
    global cards_computer_perm
    if first_time == True:
        cards_people = random.choices(cards,k=2) # Make the cards choices
        for card in cards_people:
            cards.remove(card)
        cards_computer = random.choices(cards,k=2) # Make the computer cards choices
        for card in cards_computer:
            cards.remove(card)
        cards_people_perm.append(cards_people)
        cards_computer_perm.append(cards_computer)
        first_time = False

    latest_hand = cards_people_perm[-1] 
    latest_computer = cards_computer_perm[-1] 
    points_people = sum(latest_hand)
    points_computer = sum(latest_computer)
    print(f"Your cards: {latest_hand}, current score: {sum(latest_hand)}")
    print(f"Computer's first card: {latest_computer[0]}")
    more_card = input("Type 'y' to get another card, type 'n' to pass [Y/n]: ")
    if more_card.lower() == "y":
        card_people = random.choices(cards,k=1) # Make the cards choices
        for card in card_people:
            cards.remove(card)
        card_computer = random.choices(cards,k=1)
        for card in card_computer:
            cards.remove(card)
        print(cards)
        os.system("clear")
        start()
    elif more_card.lower() == "n":
        print(f"Your final hand: {cards_people_perm}, current score: {sum(latest_hand)}")
        print(f"Computer's final hand: {cards_computer_perm}, current score: {sum(latest_computer)}")
        if points_people > points_computer:
            print("You Win!")
        elif points_people == points_computer:
            print("Draw 🙃")
        elif points_people == 0:
            print("Win with a Blackjack 😎")
        elif points_computer == 0:
            print("Lose, opponent has Blackjack!")
        else:
            print("You Lose!") 
        dowantplay = input("Do you want play blackjack? [Y/n]: ")
        if dowantplay.lower() == "y":
            start()
        

start()