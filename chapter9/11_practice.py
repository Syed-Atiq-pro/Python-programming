with open("old.txt") as f:
    content2 = f.read()

with open("rename.txt","w") as f:
    f.write(content2)
    