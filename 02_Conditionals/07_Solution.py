Order_Size=input("Enter the size of the coffee (Small, Medium, Large): ")
extra_shot=input("Do you want an extra shot of espresso? (yes/no): ")

if extra_shot=="yes":
    coffee= Order_Size + " coffee with an extra shot"

else:
    coffee=Order_Size+" coffee"

print("Order:",coffee)