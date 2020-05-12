# if statement example
a = 33
b = 200

if b > a:
    print("b is greater than a")

# shorthand if statement example
a = 200
b = 33

if a > b: print("a is greather than b")

# elif statement example
a = 33
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are eqaul")

# else statement example
a = 200
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

# shorthand if...else statement (ternary operators or conditionary expressions)
a = 2
b = 330

print ("A") if a > b else print("B")

# shorthand if...else multiple else conditions
a = 330
b = 330

print("A") if a > b else print("=") if a == b else print ("B")

# And statements
a = 200
b = 33
c = 500

if a > b and c > a:
    print("Both conditions are True")

# Or statements
if a > b or a > c:
    print("At least one of the conditions are True")

# Nested If statements
x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

# The Pass Statment
a = 33
b = 200

if b > a:
    pass