#   * 
#  ***
# *****  for n = 3

n = int(input("Enter number : "))


for i in range (n):
    space = " " * (n - i - 1)       # Here ( ' n ' is the number of rows and let n = 3 , iniaitially i = 0 ,1 ,2 )
    star = "*" * ( 2 * i + 1)       # Here(  2 is important { see here any odd number multiplies odd number = odd number  }   )
    print( space + star )

'''
    iteration 1:
    n = 3 , i = 0
    for sapce 
    3 - 0 - 1 = 2 spaces          
    for star 
    2 * 0 + 1 = 1 star          

    iteration 2:
    n = 3 , i = 1
    for space 
    3 - 1 - 1 = 1 spaces
    for star 
    2 * 1 + 1 = 3 stars

    iteration 3:
    n = 3 , i = 2
    for space
    3 - 2 - 1 = 0 spaces 
    for star
    2 * 2 + 1 = 5 stars '''

   
