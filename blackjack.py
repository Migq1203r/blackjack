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
        cards_people = [random.choice(cards), random.choice(cards)] # Make the cards choices
        for card in cards_people:
            cards.remove(card)
        cards_computer = [random.choice(cards), random.choice(cards)] # Make the computer cards choices
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
        card = random.choice(cards)
        cards_people_perm[-1].append(card)
        cards.remove(card)
        print(card)
        card = random.choice(cards)
        cards_computer_perm[-1].append(card)
        cards.remove(card)
        print(card)
        os.system("clear")
        start()
    elif more_card.lower() == "n":
        print(f"Your final hand: {cards_people_perm}, current score: {sum(latest_hand)}")
        print(f"Computer's final hand: {cards_computer_perm}, current score: {sum(latest_computer)}")
        if points_people > 21:
            print("You Lose!")
        elif points_computer > 21:
            print("You Win!")
        elif points_people > points_computer:
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
        os.system("clear")
        cards.clear()
        cards.extend([2,3,4,5,6,7,8,9,10,10,10,10,11])
        if dowantplay.lower() == "y":
            first_time = True
            start()
        

start()
