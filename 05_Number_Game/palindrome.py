n=int(input("Enter the number to be reversed "))
original_num=n
rn=0
while n!=0:
    digit=n%10
    rn=rn*10+digit
    n//=10

if rn==original_num:
    print("it is a palindrome")
else:
    print("It is not a palindrome")