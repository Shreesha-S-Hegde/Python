def name(hello,*args):
    for i in args:
        print("hello",i)

names=("Rahul","John","Shreesha","Shreya")
name("Hello",*names)