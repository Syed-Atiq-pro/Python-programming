class Calculator:
    def expo(self,n,i):
        print(f"The  number is {n**i}")

    def root(self,n):
        print(f"root is {n**1/2}")

n = int(input("Enter the number : "))
i = int(input("Enter the number of EXPO : "))
cal = Calculator()
cal.expo(n,i)
cal.root(n)

    
