with open("file1.txt","r") as f:
    str = f.read()
    # str2 = f.readline()
    # str2 = f.readlines()
    print(type(str))
    print(str)
    if "hello" in str:
        print("present")

    else:
        print("not")
    
    
