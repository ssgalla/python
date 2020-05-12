# There are four collection data types in the Python programming language:
#   List is a collection which is ordered and changeable. Allows duplicate members.
#
#   Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#
#   Set is a collection which is unordered and unindexed. No duplicate members. 
#
#   Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# create a set
set1 = {"apple", "banana", "cherry"}
print(set1)

# access items NOTE: sets do not have an index number as they are unordered so you cannot access values by index numbers
for x in set1:
    print(x)

# check if banana is present in the set
print("banana" in set1)

# add items - once a set is made you cannot change items in it but you can add items
set1.add("orange")
print(set1)

# add multiple items using the update() method
set1.update(["mango", "grapes"])
print(set1)

# get the length of a set
print(len(set1))

# remove item from a set using remove()
set1.remove("banana")
print(set1)

# remove item from set using discard()
set1.discard("cherry")
print(set1)

# empty the set using clear()
set1.clear()
print(set1)

# add items back to set
set1.update(["kiwi", "watermelon", "grapes"])
print(set1)

# new sets for tasks 
set2 = {"oranges", "apples"}
set3 = {"strawberries", "pear", "guava"}
set4 = {"pineapple", "coconut", "lychee"}

# join two sets together
# using union - will insert all items from both sets into a new set
unionset = set1.union(set2)
print(unionset)

# using update() - will insert one set into the other set
set3.update(set4)
print(set3)

# using the set() constructor to make a set
setconst = (("apple", "banana", "cherry"))
print(setconst)

# return a copy of a set using copy()
copysetconst = set3.copy()
print(copysetconst)

# return a set that contains the items that only exist in the first set and not the second using difference()
diff1 = {"apple", "banana", "cherry"}
diff2 = {"google", "microsoft", "apple"}

difference = diff1.difference(diff2)
print(difference)

# remove the items that exist in both sets using difference_update()
diff1.difference_update(diff2)
print(diff1)