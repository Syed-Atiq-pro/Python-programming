# ***
# * *
# ***

            #  Here we creating the matix with n x n so we can consider the column size is row size 

r = int(input("Enter the number"))  # rows = 5


for i in range (r):  # Here the loop will end in r times { row }

    for j in range( r):  # Here the loop will end in r times  { column } 

        if (i==0 or i == r-1 or j == 0 or j == r-1) :  # 

            print("*", end = "")

        else:

            print(" ", end="")

    print()
