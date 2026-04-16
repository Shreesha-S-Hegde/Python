n=int(input("Enter a number "))
if n==0:
    answer='neither prime nor composite'
else:

    answer='prime'
    for i in range(2,n):
        if n%i==0:
            answer='not prime'
            break
print(answer)