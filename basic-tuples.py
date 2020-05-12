# There are four collection data types in the Python programming language:
#   List is a collection which is ordered and changeable. Allows duplicate members.
#
#   Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#
#   Set is a collection which is unordered and unindexed. No duplicate members.
#
#   Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# create a tuple 
tuple1 = ("apple", "banana", "orange", "kiwi", "melon", "mango", "cherry")
print(tuple1)

# access a tuple by refering to the index numnber (banana)
print(tuple1[1])

# accessing a tuple via negative indexing (cherry)
print(tuple1[-1])

# accessing a range of indexes in a tulip
print(tuple1[2:5])

# accessing a range of indexes via negative indexes in a tulip
print(tuple1[-4:-1])

# we cannot change the value of a index in a tuple although we can convert the tuple to a list make edits then convert back to tuple 
tuplelistconv = list(tuple1)
tuplelistconv[1] = "jackfruit"
tuple1 = tuple(tuplelistconv) 
print(tuple1)

# loop through a tuple
for x in tuple1:
    print(x)

if "apple" in tuple1:
    print("Yes, tuple1 does contain the item apple.")

# find the length of a tuple
print(len(tuple1))

# create a tuple with only one item in it 
singletuple = ("apple",)
print(type(singletuple))

# join two tuples
tuple2 = ("brocolli", "cabbage", "mushroom", "carrots")
jointtuple = tuple1 + tuple2
print(jointtuple)

# make a tuple using tuple(constructor)
tupleconst = tuple(("html", "css", "python", "C++"))
print(tupleconst)

# count how many times a value appears in a tuple
x = tupleconst.count("html")
print(x)

# search for a value and return its position within a tuple
x = tupleconst.index("html")
print(x)