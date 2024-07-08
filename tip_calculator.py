print("Welcome to the tip calculator")
total_bill=float(input("What was the total bill?$"))
percentage=int(input("What percentage tip would you like to give? 10,12, or 15?"))
no_of_people=int(input("How may people to split the bill?"))
payment=total_bill*(1+percentage/100)/no_of_people
payment=round(payment,2)
payment="{:.2f}".format(payment)
print(f"Each person should pay: $ {payment}")

