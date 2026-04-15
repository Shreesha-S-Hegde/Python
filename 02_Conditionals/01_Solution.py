age=int(input("Enter your age in years: "))
if age<13 and age>=1:
    print("You are a child.")
elif age>=13 and age<19:
    print("You are a teenager.")
elif age>=19 and age<=59:
    print("You are an adult.")
elif age>=60:
    print("You are a senior citizen.")
else:
    print("Invalid age.")