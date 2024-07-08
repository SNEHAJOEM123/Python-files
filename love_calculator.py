print("Welcome to the Love Calculator")
name1=input("What is your name?")
name2=input("What is their name?")
combined_string=name1+name2
lowercase_combined_string=combined_string.lower()

t=lowercase_combined_string.count("t")
r=lowercase_combined_string.count("r")
u=lowercase_combined_string.count("u")
e=lowercase_combined_string.count("e")
true=t+r+u+e

l=lowercase_combined_string.count("l")
o=lowercase_combined_string.count("o")
v=lowercase_combined_string.count("v")
e=lowercase_combined_string.count("e")
love=l+o+v+e

love_score=str(true)+str(love)
love_score=int(love_score)

if love_score<10 or love_score>90:
    print(f"Your love score is {love_score}, you go together like coke and mentos")

elif  love_score>=40 and love_score<=50:
    print(f"Your love score is {love_score}, you are alright together.")

else:
    print(f"Your score is {love_score}")
    





