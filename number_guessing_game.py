import random
from number_guessin_game_art import logo
EASY_LEVEL_TURNS=5
HARD_LEVEL_TURNS=10


def set_difficulty():
    level=input("Choose a difficulty.Type 'easy' or 'hard':")
    if level=='easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS



def check_answer(guess,answer):
    global turns
    if guess>answer:
            print("Too high")
    elif guess<answer:
            print("Too low")
    else:
        print(f"You got it!.The answer was {answer}")

def game():  
    print(logo)     
    print("Welcome to the Number Guessing Game")
    print("I'm thinking of a number between 1 and 100")
    
    answer=random.randint(1,100)
    turns=set_difficulty()
    guess=0
    while guess!=answer and turns>0:
        print(f"You have {turns} attempts to guess the number")
        guess=int(input("Make a guess:"))
        turns-=1
        check_answer(guess,answer)
        if turns>0:
             print("Guess Again")
        
    if turns==0:    
      print("You have run out of guesses. You lose")
game()





