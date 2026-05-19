sub1=int(input("Enter the marks of subject : "))
sub2=int(input("Enter the marks of subject : "))
sub3=int(input("Enter the marks of subject : "))

# cheching the total percentage of the student marks
total_percentage = ((sub1 + sub2 + sub3)*100)/300

if(total_percentage > 40 and sub1 > 33 and sub2 > 33 and sub3 > 33):
    print("you are pass",total_percentage)

else:
    print("you fail!",total_percentage)
    