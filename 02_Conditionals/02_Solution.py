# age = int(input("enter your age:"))
# day=input("Enter the day")
# ticket=0
# if age<18:
#     ticket=8
# elif age>=18:
#     ticket=12
# if day=="Wednesday":
#     ticket=ticket-2
# print("Ticket price for you is",ticket)
age = int(input("enter your age:"))
day = "Wednesday"

price = 8 if age<=18 else 12

if day== "Wednesday":
    # price=price-2
    price-=2

print("Ticket price for you is",price)