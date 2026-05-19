p1="hello"
p2="scam"
p3="money"
p4="mac"

message = input("Enter the comment : \n")

if(p1 in message or p2 in message or p3 in message or p4 in message ):
    print("It seems like it a scam! , be aware of it")

else:
    print("It not a scam , you can proseed ")