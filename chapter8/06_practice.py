# Converting inches into cm 
# inch = 2.54 cm

def inch(n):
    if n == 0:
        return
    print(f"the inches to cm is : {n*2.54}")

n = int(input("Enter the number : "))
inch(n)