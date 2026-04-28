def sum(*args):
    sum=0
    for item in args:
        sum+=item
    print(sum)

numbers=(1,2,35,7,67)
sum(*numbers)