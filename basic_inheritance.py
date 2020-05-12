# create a parent class then create object and use printname method
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

x = Person("John", "Doe")
x.printname()

# create a child class that inherits functionality from another class (parent/child relationship)
class Student(Person):
    pass

x = Student("Shaminder", "Galla")
x.printname()

# using __init__() func in child class
# when we use the __init__() func in a child class we must call back to parent class inside func else we lose inheritance and the child object becomes its own object

#class Student(Person):
    #def __init__(self, fname, lname):
        #Person.__init__(self, fname, lname) #calling back to parent function for inheritance

# using the super() function that will make the child class inherit all the methods and properties from its parent
# by using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        # add properties
        self.graduationyear = year

x = Student("Mike", "Olsen", 2019)