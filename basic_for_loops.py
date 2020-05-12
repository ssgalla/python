# for loops example
fruits = ["apple", "banana", "cherry"]

for x in fruits:
    print(x)

# looping through a string 
for x in "banana":
    print(x)

# the break statement can stop the loop before it has looped through all the items
for x in fruits:
    print(x)
    if x == "banana":
        break

# continue statement can stop the current iteration of the loop and continue with the next
for x in fruits:
    if x == "banana":
        continue
    print(x)

# loops through a set of code a specified number of times using range()
for x in range(6):
    print(x)

for x in range(2, 6):
    print(x)

# using range() to loop through a set of code we can also add a third parameter which will allow us to change the incremental value of each step
for x in range( 2, 30, 3):
    print(x)

# else in for loop 
for x in range(6):
    print(x)
else:
    print("Finally finished!")

# nested loops - the inner loop will be executed one time for each iteration of the "outer loop"
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

# Pass statements - a for loops cannot be empty but if you have a for statement with no content put a pass init to avoid an error
for x in [0, 1, 2]:
    pass