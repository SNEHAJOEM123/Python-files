import random
names_string=input("Give me everybody's name separated by a comma\n")
names=names_string.split(",")
l=len(names)-1
random_choice=names[random.randint(0,l)]
print(random_choice)

