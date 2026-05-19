class Calculator:
    def expo(self,n,i):
        print(f"The  number is {n**i}")

    def root(self,n):
        print(f"root is {n**1/2}")
    @staticmethod
    def hello():
        print("Hello Thnaks for using Calculator")

n = int(input("Enter the number : "))
i = int(input("Enter the number of EXPO : "))
cal = Calculator()
cal.expo(n,i)
cal.root(n)
cal.hello()

    
