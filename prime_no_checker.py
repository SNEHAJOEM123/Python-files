def prime_checker(number):
    is_prime=True
    for i in range(2,number):
        if (number%i==0):
            is_prime=False
            break
    if is_prime==True:
        print(f"{number} is a prime number")   
    else:
        print(f"{number} is not a prime number")

n=int(input("Enter the number to be checked:"))
prime_checker(n)            