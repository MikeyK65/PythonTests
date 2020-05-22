# classes

class Rectangle:
    width = 10
    height = 20

    def getArea (self):
        return self.width * self.height

# Create objects
myRect1 = Rectangle()
myRect2 = Rectangle()

# Set one of the rectangles to a non-default widdth
myRect2.width = 5


class Employee:
    empCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    def __str__(self): # used by print method
        return self.name + " : " + str(self.salary)

employee = Employee("John", 50000)

print (employee.name)
print (employee.salary)
print (Employee.empCount)

employees = [
    Employee("Mike", 10000),
    Employee("alan", 20000),
    Employee("jane", 40000),
    Employee("jonny", 100000),
    Employee("Nick", 200000),
    Employee("Steve", 17000)
    ]

for e in employees:
    print (e)

print (Employee.empCount)

