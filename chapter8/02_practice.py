# temparature converter 

# c/5 = (f-32)/9
# c = 5*(f-32)/9
# f = 5/9 *( c+ 32)

def temp():
    print("if you want to conavert f to c then press f ")
    t = input("Enter mode :")
    n = int(input("Enter the number:"))
    if t == "f":

        c = n
        f = ( c * 9/5 ) + 32
        print(f)

    else:
        f = n
        c = 5*(f-32)/9
        print(c)

temp()

