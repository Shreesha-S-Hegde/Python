def myfunction(*args):
    print("FIrst arguement is",args[0])
    print("Second arguement is",args[1])
    print("All arguements are",args)
    print(type(args))

myfunction(1,2,3)