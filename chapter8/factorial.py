# recursions

# creating a function also called as function definition

def factorial(n):

    if(n==0 or n==1) :
        return 1

    return n * factorial(n-1)
n = int(input("Enter number : "))

a=0
for i in range (n):
    a=factorial(n)


print( f"factorial is {a}")



