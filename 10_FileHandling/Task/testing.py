# f=open("testcase.txt","x")

with open("testcase.txt","w") as f:
    f.write("Hello world\n")
    f.write("Hello everyone")

# with open("testcase.txt","a") as f:
#     f.write("File Handling")
#     f.write("Help")

with open("testcase.txt","r") as f:
    print(f.read())