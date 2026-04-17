import random
answer=input("Do you want to play the game(yes/no)")
if answer=='yes':
    a=random.randint(1,6)
    b=random.randint(1,6)
    print("The numbers in the dice are",a,b)
elif answer=='no':
    print("Thank you for playing")
else:
    print("Invalid input")