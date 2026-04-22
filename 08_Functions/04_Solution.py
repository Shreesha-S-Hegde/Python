import math
r=int(input("Enter radius:"))
def circumference_area(r):
    circumference=2*(math.pi)*r
    area=math.pi*(r*r)
    return(circumference,area)
print("The circumference and area of the circle are",circumference_area(r))