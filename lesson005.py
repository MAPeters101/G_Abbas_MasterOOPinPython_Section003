class Employee:
    name = "Paul"
    age = 25
    salary = 10000

    def getSalary(self):
        return self.salary

paul = Employee() # Creating object of Employee class
print(paul.getSalary())
print(paul.age)

