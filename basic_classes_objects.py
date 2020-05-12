# class creation example
class MyClass:
    x = 5

# object creation example
p1 = MyClass()
print(p1.x)

# using the __init__() function
# the self parameter is what is used to access values within the class... this can be called whatever you wish
# Note: The __init__() function is called automatically every time the class is being used to create a new object.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Shaminder", 26)

print(p1.name)
print(p1.age)

# object methods - create a function within a class
class Person:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("Shaminder", 26, "gurgaon")
p1.myfunc()

# modify object properties
p1.age = 40
print(p1.age)

# delete object properties
del p1.location

# pass statements - class defnitions cannot be empty but if it is use pass to avoid error
class Person: 
    pass