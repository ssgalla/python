# There are four collection data types in the Python programming language:
#   List is a collection which is ordered and changeable. Allows duplicate members.
#
#   Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#
#   Set is a collection which is unordered and unindexed. No duplicate members.
#
#   Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# create a list - all lists are zero indexed for apple is 0 and banana is 1
list1 = ["apple", "banana", "orange", "kiwi", "strawberry", "mango"]

# how to access list as a whole and individually
# access full list
print(list1)

# access second item (banana)
print(list1[1])

# negative indexing (mango) - this will allow you to access the list from the end
print(list1[-1])

# range of indexes (orange:strawberry) - how to view a section of the list
print(list1[2:5])

# range of negative indexes (kiwi:strawberry) - how to view a section of the list the from end of the list
print(list1[-3:-1])

# change item in a list - how to go into a list and be able to change items
list1[0] = "watermelon"
print(list1)

# loop through a list
for x in list1:
    print(x)

# determine if item exists in list
if "watermelon" and "mango" in list1:
    print("Yes, watermelon and mango is in the list.")

# determine length of list using len()
print(len(list1))

# add an item to the end of the list using append()
list1.append("apple")
print(list1)

# add an item to list at specified location in list using insert()
list1.insert(1, "orange")
print(list1)

# remove specified item from list
list1.remove("apple")
print(list1)

# remove last indexed item or specified item in list using pop()
list1.pop(1) # use index number of item in list if you wish to specify NOTE: lists are zero indexed
list1.pop()
print(list1)

# remove specified index using del()
del list1[2]
print(list1)

# delete entire list using del()
del list1

# create a new list 
list2 = ["ford", "ferrari", "lamborghini", "audi", "mercedes-benz"]
list3 = ["tesla", "volkswagen", "maybach", "hyundai", "tata"]
print(list2)

# copy a list using list()
copylist2 = list(list2)
print(copylist2)

# join two lists
jointlist23 = list2 + list3
print(jointlist23)

# join two lists using extend() NOTE: this will join two lists without making a new list 
# list2.extend(list3)

# sort a list 
jointlist23.sort() #alphabetically
print(jointlist23)

jointlist23.sort(reverse=True) #descending
print(jointlist23)
