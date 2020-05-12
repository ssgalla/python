# creating a function
def intro_function():
    print("Hello from a function")

intro_function()

# arguments in a function are inputs that go into a function
def argument_function(fname):
    print(fname + " Refsnes")

argument_function("Emil")
argument_function("Tobias")
argument_function("Linus")

# number of arguments
def doubleargument_function(fname, lname):
    print(fname + " " + lname)

doubleargument_function("Shaminder", "Galla")
doubleargument_function("Satvinder", "Galla")

# arbitary arguments (*args) - if you do not know how many arguemnts will be passed to your function add a * before parameter name in func def
def arbitaryargs(*kids):
    print("The youngest siblings are " + kids[0] + " and " + kids[1])

arbitaryargs("Shaminder", "Simran", "Sanjit")

# keyword arguments - you can also send arguments with the key = value syntax
def keywordarguments(child1, child2, child3):
    print("The youngest child is " + child1 + " , the second youngest is " + child2 + " and the eldest is " + child3)

keywordarguments(child1 = "Shaminder Galla", child2 = "Simran Galla", child3 = "Sanjit Galla")

# arbitary keyword arguments (**kwargs) - if you do not know how many keyword arguments there will be you can add ** before the parameter name 
def kwargs_function(**kid):
    print("His last name is " + kid["lname"])

kwargs_function(fname = "Tobias", lname = "Refsnes")

# default parameter value - if we called this function without an argument its output would automatically be Norway
def paramvalue_definition(country = "Norway"):
    print("I am from " + country)

paramvalue_definition("Sweden")
paramvalue_definition("India")
paramvalue_definition()
paramvalue_definition("Brazil")

# passing a list as an argument
def fruit_function(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]

fruit_function(fruits)

# return values
def return_function(x):
    return 5 * x

print(return_function(3))
print(return_function(5))
print(return_function(9))

# pass statement - functions cannot be without conntent but if for some reason it is place pass inside function to avoid error
def pass_function():
    pass

# CHECK ONLINE FOR RECURSION UNDERSTANDING