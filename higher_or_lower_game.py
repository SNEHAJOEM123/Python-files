from higher_or_lower_art import logo,vs
from higher_or_lower_data import data
import random
import os

def game():
    score=0
    end_of_game=False
    print("WELCOME TO THE HIGHER OR LOWER GAME")
    print(logo)
    a=random.choice(data)
    b=random.choice(data)
    
    while not end_of_game:
        while(a==b):
           b=random.choice(data)
        
        print(f"Compare A: {a['name']},a {a['description']},from {a['country']}.")
        print(vs)
        print(f"Against B: {b['name']},a {b['description']},from {b['country']}.")  
        choice=input("Who has more followers? Type 'A' or 'B':").lower()
        if choice=='a' and a['follower_count']>b['follower_count']:
            score+=1
            a=b
            b=random.choice(data)
            while(a==b):
               b=random.choice(data)
            os.system('cls')
            print(logo)
            print(f"You are right! Current Score: {score}")
        elif choice=='b' and b['follower_count']>a['follower_count']:   
            score+=1
            a=b
            b=random.choice(data)
            while(a==b):
               b=random.choice(data)
            os.system('cls')
            print(logo)
            print(f"You are right! Current Score: {score}")
        else:
            end_of_game=True
            print(f"You are wrong!Your Final score: {score}")
            print("Game Over")


game()
