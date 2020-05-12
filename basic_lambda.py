# lambda function addition example
x = lambda a : a + 10
print(x(5))

# lambda function multiplier example
x = lambda a, b : a * b
print(x(5, 6))

# lambda function that sums argument a, b, c 
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

# lambda functions work better within a function - this function uses lambda to always doulbe the number inside it
def lambdadoublefunc(n):
    return lambda a : a * n

mydoubler = lambdadoublefunc(2)

print(mydoubler(11))

# this function will always triple the number passed to it
def lambdatriplefunc(n):
    return lambda a : a * n

mytripler = lambdatriplefunc(3)

print(mytripler(11))

# we can also use one program to execute both of these
def lambdafunc(n):
    return lambda a : a * n

mydoubler = lambdafunc(2)
mytripler = lambdafunc(3)

print(mydoubler(22))
print(mytripler(22))

# you can use lambda functions when an anonymouse function is required for a short amount of time