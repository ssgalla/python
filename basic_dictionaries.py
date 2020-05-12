# There are four collection data types in the Python programming language:
#   List is a collection which is ordered and changeable. Allows duplicate members.
#
#   Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#
#   Set is a collection which is unordered and unindexed. No duplicate members. 
#
#   Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# create and print a dictionary
dict1 = {
    "brand": "Mercedes",
    "model": "S350d",
    "year": "2016"
}
print(dict1)

# accessing items in a dictionary
modeldict = dict1["model"]
print(modeldict)

# accesing items using get()
modeldict = dict1.get("model")
print(modeldict)

# changing values in a dictionary
dict1["brand"] = "Mercedes-Benz"
print(dict1.get("brand"))

# loop through a dictionary 
for x in dict1:
    print(x)

# loop through and print all values in dictionary 
for x in dict1:
    print(dict1[x])

# how to return all values in dictionary using values()
for x in dict1.values():
    print(x)

# how to return both keys and values in a dictionary by using items()
for x,y in dict1.items():
    print(x, y)

# check if a key exists in the dictionary
if "model" in dict1:
    print("Yes, a key is present in this dictionary")

# determine the length of a dictionary (one record is both a key-value pair)
print(len(dict1))

# adding items to a dictionary
dict1["color"] = "White"
print(dict1)

# remove item from dictionary with specified key name using pop()
dict1.pop("model")
print(dict1)

# remove last inserted item from dictionary using popitem()
dict1.popitem()
print(dict1)

# remove items using DEL
del dict1["year"]
print(dict1)

# delete entire dictionary using DEL
del dict1

# create new dictionaries
cardict = {
    "brand": "ford",
    "model": "fiesta titanium",
    "year": "2014"
}

citydict = {
    "london": "united kingdom",
    "birmingham": "united kingdom",
    "gurgaon": "india"
}

hometowndict = {
    "wolverhampton": "united kingdom"
}

# clear dictionary using clear()
hometowndict.clear()
print(hometowndict)

# make a copy of a dictionary using copy()
cardictcopy = cardict.copy()
print(cardictcopy)

# make a copy of a dict using dict()
citydictcopy = dict(citydict)
print(citydictcopy)

# making a nested dictionary - a dictionary with multiple dictionaries inside of it 
myfamily = {
    "sibling1" : {
        "first name" : "sanjit",
        "surname" : "galla",
        "year" : 1986
    },
    "sibling2": {
        "first name" : "simran",
        "surname" : "galla",
        "year" : 1990
    },
    "mother" : {
        "first name" : "satvinder",
        "surname" : "galla",
        "year" : "n/a"
    },
    "father" : {
        "first name" : "onkar",
        "surname" : "galla",
        "year" : "n/a"
    }
}
print(myfamily)

# make a dictionary using the dict() constructor
dictconst = dict(brand="toyota", model="fortuner", year=2011)
print(dictconst)