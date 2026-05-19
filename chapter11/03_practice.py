class Employee:
    def __init__(self,salary,increment): #  __init__ is a constructor used to initallize the variables or attribute

        self.salary = salary
        self.increment = increment 

    # salary = 230
    # increment = 20
    @property # property decorator is used return the any value and it called in decorator type only
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100))
    

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,newSalary):
        self.increment = ((newSalary - self.salary)/self.salary)*100



e = Employee(50000,10)
print(e.salaryAfterIncrement)
e.salaryAfterIncrement=60000
print(e.increment)