class Demo:
    a = 4

p = Demo()
# here created the object called p
print(p.a)
# printing the value of a before changing
p.a = 0
# Here we change the value of a so it will not change the class attribute insted it will create instance attribute
print(p.a)
# printing the changed value
print(Demo.a)
# Here printed the class value again , it not effect the class value bcoz of the Demo class contain no instance attribute