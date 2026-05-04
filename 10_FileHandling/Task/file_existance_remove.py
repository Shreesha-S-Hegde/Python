import os
if os.path.exists("testcase.txt"):
    os.remove("testcase.txt")
else:
    print("Doesn't exist")