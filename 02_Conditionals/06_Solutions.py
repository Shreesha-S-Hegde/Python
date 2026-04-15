Dist = int(input("Enter the distance to be covered: "))

if Dist<3:
    Transport="Walk"

elif Dist<15:
    Transport="Bike"

else:
    Transport="Car"

print(Transport)