import random
from hangman_words import word_list
from hangman_art import logo,stages

logo=logo[0]
print(logo)
chosen_word=random.choice(word_list)
print(chosen_word)
l=len(chosen_word)
display=[]
for i in range(l):
    display.append("_")
end_of_game=False    
lives=7
print(f"The word you have to guess is of {l} letters\n")
for i in range(len(display)):
        print(display[i],end=" ")  
print("\n") 


while not end_of_game:
    guess=input("Guess a letter:").lower()
    if guess in chosen_word:
        if guess in display:
            print(f"You have already guessed letter {guess}")
        else:
            print("Your guess was correct!")    
    for position in range(l):
        if guess==chosen_word[position]:
            display[position]=guess
    if guess not in chosen_word:
        print(f"You guessed {guess},that's not in the word.You lose a life")
        lives-=1
        if lives==0:
            end_of_game=True
            print("You lose")     
    if "_" not in display:
        end_of_game=True
        print("You win!")
    for i in range(len(display)):
        print(display[i],end=" ")  
    print("\n")      
    print(stages[lives])