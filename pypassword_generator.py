import random

letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','#','$','%','&','(',')','*','+']
l=len(letters)-1
n=len(numbers)-1
s=len(symbols)-1

print("Welcome to the PyPassworrd Generator")
no_of_letters=int(input("How many letters would you like in your password?\n"))
no_of_numbers=int(input("How many numbers would you like in your password?\n"))
no_of_symbols=int(input("How many symbols would you like in your password?\n"))

password=[]
for i in range(0,no_of_letters):
    password.append(random.choice(letters))
for j in range(0,no_of_numbers):
    password.append(random.choice(numbers))
for k in range(0,no_of_symbols):
    password.append(random.choice(symbols))
random.shuffle(password)
print("The random generated password is:",end=" ")
for i in password:
    print(i,end="")
