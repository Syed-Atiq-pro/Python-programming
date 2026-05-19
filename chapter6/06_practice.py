# 90-100 = EX
# 80-90 = A
# 70-80 = B
# 60-70 = C
# 50-60 = D
# <50 = F

print("""90-100 = EX
80-90 = A
70-80 = B
60-70 = C
50-60 = D
<50 = F""")

# Enetering the student name 
name = input("Enter your name: ")
# Entering the student marks

marks = int(input(f"Enter {name} marks : "))

if(marks > 90 and marks <= 100):
    print(f"{name} get \'EX\' with {marks} marks")

elif(marks > 80 and marks <= 90):
    print(f"{name} get \'A\' with {marks} marks")

elif(marks > 70 and marks <= 80):
    print(f"{name} get \'B\' with {marks} marks")

elif(marks > 60 and marks <= 70):
    print(f"{name} get \'C\' with {marks} marks")

elif(marks > 50 and marks <= 60):
    print(f"{name}u get \'D\' with {marks} marks")

else:
    print(f"{name} get \'F\' with {marks} marks")


