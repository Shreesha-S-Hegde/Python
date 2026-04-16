import random
guess_the_number=random.randint(1,100)

while True:
    guess=int(input("Enter your guess "))
    if guess<guess_the_number:
        print("Too low")
    elif guess>guess_the_number:
        print("Too high")
    else:
        print("Congratulations")
        break