thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

mylist = ["apple", "banana", "cherry"]
for i in range(len(mylist)):
  print(mylist[i])

hislist = ["apple", "banana", "cherry"]
i=0
while i<len(hislist):
  print(hislist[i])
  i=i+1

yourlist = ["apple", "banana", "cherry"]
[print(x) for x in yourlist]