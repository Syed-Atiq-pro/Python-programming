# To print the sum of n natural numbers using recursions

def add(n):
    if n == 1 :
        return 1
    return n + add(n-1)
   

n = int(input("Enter the number : "))
l = add(n)
print(l)