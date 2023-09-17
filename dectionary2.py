#Python - Loop Dictionaries
#Loop Through a Dictionary
#You can loop through a dictionary by using a for loop.
'''
When looping through a dictionary, the return value are the keys of the dictionary, but there are
methods to return the values as well.'''

#Example
#Print all key names in the dictionary, one by one:
'''
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)'''

#Example
#Print all values in the dictionary, one by one:
'''
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(thisdict[x])'''
#Example
#You can also use the values() method to return values of a dictionary:
'''
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)'''
#Example
#You can use the keys() method to return the keys of a dictionary:
'''
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.keys():
  print(x)'''
#Example
#Loop through both keys and values, by using the items() method:
'''
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)
'''


#Python - Copy Dictionaries
#Copy a Dictionary
'''
You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and 
changes made in dict1 will automatically also be made in dict2.
There are ways to make a copy, one way is to use the built-in Dictionary method copy().'''

#Example
#Make a copy of a dictionary with the copy() method:
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)'''

#Another way to make a copy is to use the built-in function dict().

#Example
#Make a copy of a dictionary with the dict() function:
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)'''


myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)


