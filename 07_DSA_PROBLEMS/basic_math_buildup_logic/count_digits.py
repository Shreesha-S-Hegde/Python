n=int(input("Enter the number:"))
answer=[]
original=n
while n!=0:
    digit=n%10
    n//=10
    answer.append(digit)
print("The number of digits is",len(answer))