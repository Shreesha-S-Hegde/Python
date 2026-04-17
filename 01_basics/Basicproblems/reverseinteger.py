n=int(input("Enter the number to be reversed "))
rn=0
while n!=0:
    digit=n%10
    rn=rn*10+digit
    n//=10
print(rn)