
with open("log.txt") as f:
    lines = f.readlines()
l=1
for line in lines:
    if  "python" in line :
        print("is in line",l)
        break
    l += 1

else:
    print("not exist")


# if "python" in content:
#     print("present")

# else:
#     print("Not present")