'''
The Deck is unlimited in size.
There are no jokers.
The Jack/King/Queen all count as 10.
The Ace can count as 1 or 11.
'''
import random
import os
import sys
from blackjack_art import logo

def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card

def calculate_score(cards):
    '''Takes a list of cards and return the score calculated from the cards'''
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score,computer_score):
    if user_score==computer_score:
        return "Draw"
    elif user_score==0:
        return "You win with a Blackjack"
    elif computer_score==0:
        return "You lost.Computer has a Blackjack"
    elif user_score>21:
        return "You went over.You lose"
    elif computer_score>21:
        return "Computer went over.You win"
    elif user_score>computer_score:
        return "You win"
    else:
        return "You lose"
    
def play_game():
    print("WELCOME TO THE GAME OF BLACKJACK")
    print(logo)    
    user_cards=[]
    computer_cards=[]
    is_game_over=False

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:    
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f"Your cards :{user_cards}, Current score:{user_score}")
        print(f"Computer's first card :{computer_cards[0]}")

        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over=True
        else:
            choice=input("Type 'y' to get another card,type 'n' to pass:")
            if choice=='y':
                user_cards.append(deal_card())
            else:
                is_game_over=True    

    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)

    print(f"Your final hand :{user_cards},final score:{user_score} ")
    print(f"Computer's final hand:{computer_cards},final score:{computer_score}")
    print(compare(user_score,computer_score))

    want_to_play=input("Do you want to continue playing the game of Blackjack? Type 'y' or 'n':")
    while want_to_play=='y':
        os.system("cls")
        play_game()
    else:
        sys.exit()    

want_to_play=input("Do you want to play the game of Blackjack? Type 'y' or 'n':")
if want_to_play=='y':
    play_game()
else:
    sys.exit()    