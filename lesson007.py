class Employee:
    # Class attribute
    companyName = "ABC"

    # Using instance attributes here
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    # Instance Methods
    def showEmployeeDetails(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)
        print("Company:", self.companyName)

    # Static method
    @staticmethod
    def getCompanyInfo():
        print("This company was founded in early days of 2015.  Welcome to this company.")


Employee.getCompanyInfo()

paul = Employee("Paul", 25, 5000)
paul.getCompanyInfo()