# local scope
# a variable created inside a function belongs to the local scope of that function, and can only be used inside that function
def myfunc():
  x = 300
  print(x)

myfunc()

# function inside function
# the variable x is not available outside the function, but it is available for any function inside the function
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

# global scope
# a variable created in the main body of the Python code is a global variable and belongs to the global scope
x = 300

def myfunc():
  print(x)

myfunc()

print(x)

# naming variables
# if you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function)
x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)

# global keyword
# if you need to create a global variable, but are stuck in the local scope, you can use the global keyword
def myfunc():
  global x
  x = 300

myfunc()

print(x)