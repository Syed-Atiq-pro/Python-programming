# finding the largest number among 3 numbers

def lar(a,b,c):
    num = max(a,b,c) # also use min()
    return num

a=int(input("Enter the number"))
b=int(input("Enter the number"))
c=int(input("Enter the number"))

d = lar(a,b,c)

print(d)