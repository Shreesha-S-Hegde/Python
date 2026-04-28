numbers=(1,2,35,7,67)
def maximum(*args):
    for i in args:
        max=0
        if i>=max:
            max=i
    return max

print("The maximum of the numbers is",maximum(*numbers))