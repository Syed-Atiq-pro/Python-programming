#creating a multiplication table 
num = int(input("Enter the number for multiplacation table:"))

for i in range ( 1,11):
    print(f"{num}X{i}={i*num}")