# replacing the Donkey word with ######

word = "Donkey"

with open("file4.txt") as f:
    content = f.read()
    newContent = content.replace(word,"######")

with open("file4.txt","w") as s:
    s.write(newContent)
