class Employee:

    # This is class attribute
    companyName = "ABC LLC"

    # These are instance attributes
    name = "Chris"
    age = 29
    salary = 5000

    def getSalary(self):
        return self.salary

chris = Employee()
paul  = Employee()
print(chris.companyName)
print(paul.companyName)

Employee.companyName = "XYZ LLC"
print(chris.companyName)
print(paul.companyName)

paul.name = "Paul"
print(paul.name)
print(chris.name)
print('-'*80)

Employee.companyName = "ABC LLC"
print(chris.companyName)
print(paul.companyName)

paul.companyName = "XYZ LLC"
print(paul.companyName)
print(chris.companyName)


