n=int(input("Enter the number of elements in the list "))
count=0
list=[]
for i in range(n):
    elements=int(input("Enter element "))
    list.append(elements)
print(list)

for item in list:
    if item>=0:
        count+=1
print("The number of positive numbers in the list are",count)