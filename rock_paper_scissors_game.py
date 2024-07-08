import random
user_choice=int(input("What do you choose?Type 0 for Rock,1 for Paper or 2 for Scissors.\n "))

if user_choice>=3 or user_choice<0:
    print("You have entered an invalid number. You lose!")

else:
    if user_choice==0:
        print("You chose rock")
    elif user_choice==1:
        print("You chose paper")
    elif user_choice==2:
        print("You chose Scissors")



    computer_choice=random.randint(0,2)

    if computer_choice==0:
        print("Computer chose rock")
    elif computer_choice==1:
        print("Computer chose paper")
    elif computer_choice==2:
        print("Computer chose Scissors")


    if user_choice==2 and computer_choice==0:
        print("You lose!")
    elif user_choice==0 and computer_choice==2:
        print("You win!")    
    elif user_choice>computer_choice:
        print("You won!")
    elif user_choice<computer_choice:
        print("You lose")    
    elif user_choice==computer_choice:
        print("Its a draw")    
    
