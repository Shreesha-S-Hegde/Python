answer=0
while True:
    n=int(input("Enter number "))
    if n!=0:
        answer+=n
    elif n==0:
        print(answer)
        break