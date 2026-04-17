thislist=["orange","mango","kiwi","banana","pineapple"]
thislist.sort()
print(thislist)

thislist=["orange","mango","kiwi","banana","pineapple"]
thislist.sort(reverse=True)
print(thislist)

thislist.sort(key=str.lower)
print(thislist)