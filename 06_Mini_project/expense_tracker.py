expenditure=[]
total_expense=0
while True:
    print("\n======= MENU =======")
    print("1️⃣   Add Expense")
    print("2️⃣   View All Expenses")
    print("3️⃣   View Total Spending")
    print("4️⃣   Exit")
    print("=====================")
    choice=int(input("Enter your choice(1-4):"))
    #Add expense
    if choice==1:
        date=input("Enter date(DD/MM/YYYY):")
        category=input("Enter category(Food,Shopping,etc:)")
        description=input("Enter short description:")
        amount=int(input("Enter amount:"))
        print("Successfully added")

        expense={"date":date,"category":category,"description":description,"amount":amount}
        expenditure.append(expense)
        total_expense+=amount

    elif choice==2:
        for exp in expenditure:
            print("Date:", exp["date"],
                      "| Category:", exp["category"],
                      "| Description:", exp["description"],
                      "| Amount:", exp["amount"])

    elif choice==3:
        print(total_expense)

    elif choice==4:
        print("Successfully exited")
        break

    else:
        print("Enter valid input")