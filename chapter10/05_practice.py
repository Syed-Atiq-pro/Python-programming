from random import randint
class Train:
    def book(self,trainNo,fro,to):
        print(f"your ticket is booked from {fro} to {to} and your train number is {trainNo}")
    def getStatus(self,trainNo):
        print(f"tarin is comming your train number is {trainNo}")

    def getFare(self,trainNo,fro,to):
        print(f"your ticket is booked from {fro} to {to} and your train number is {trainNo} . Your Fare is{randint(222,555)}")

sc = Train()
sc.book(1,"vijayawada","chennai")
sc.getStatus(1)
sc.getFare(1,"vijayawada","chennai")