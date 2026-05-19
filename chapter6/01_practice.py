a=int(input("Enter  the number :"))
b=int(input("Enter  the number :"))
c=int(input("Enter  the number :"))
d=int(input("Enter  the number :"))

print("program is starting \n")
if(a > b and a > c and a >d):
    print(f"A is biggest number {a}\n")

elif(b > a and b > c and b > d):
    print(f"B is biggest  number {b}\n")

elif(c > a and c > b and c > d):
    print(f"C is biggest number {c}\n")

else:
    print(f"D is biggest number {d}\n")

print("end of the  program")