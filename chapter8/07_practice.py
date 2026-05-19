# strip()

def rem(l,word):
    n = []
    for item in l:
        if not ( word == item ):
            n.append(item.strip(word))
    return n

l = ["harry","atiq","nishu","arry"]
word = input("Enter any word")

print(rem(l,word))

# Example:
#     "__Hello__"
#     rstrip(__) __Hello
#     lstrip(__) Hello__
#     strip(__) Hello

