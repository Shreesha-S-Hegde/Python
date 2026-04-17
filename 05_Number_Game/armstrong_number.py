n=int(input("Enter a number "))
am=0
length=len(str(n))
original_num=n
while n!=0:
    digit=n%10
    am=(digit**length)+am
    n//=10
if original_num==am:
    print("It is an armstrong number")
else:
    print("It is not an armstrong number")