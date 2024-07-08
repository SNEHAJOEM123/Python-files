print("welcome to the rollercoaster")
height=int(input("what is your height in cm?"))
bill=0
if height>120:
   print("You can ride the rollercoaster")
   age=int(input("What is your age?"))
   if (age<12):
       bill=5
   elif(age<=18):
       bill=7
   elif age>=45 and age<=55:
       print("Everything is going to be ok. Have a free ride with us")     
   else:
        bill=12 

   wants_photo=input("Do you want photo taken? Y or N :")
   if wants_photo=='Y': 
       bill+=3
   print(f"Your final bill is {bill}")    
else:
    print("You cannot ride the rollercoaster")    