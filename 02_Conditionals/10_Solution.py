pet=input("Enter the pet you have ")
age=int(input("Enter the age of the pet "))
if pet=='dog':
    if age<2:
        print("puppy food")
    elif age<5:
        print("adult dog food")
    else:
        print("senior dog food")
if pet=='cat':
    if age<2:
        print("kitten food")
    elif age<5:
        print("adult cat food")
    else:
        print("senior cat food")