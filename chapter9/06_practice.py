with open("log.txt") as f:
    content = f.read()

if "python" in content:
    print("present")

else:
    print("Not present")