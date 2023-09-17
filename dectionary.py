#Dictionary
'''
Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
Dictionaries are written with curly brackets, and have keys and values:'''
#Example
#Create and print a dictionary:
'''
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)'''

#Python Dictionary Methods
#Python has a set of built-in methods that you can use on dictionaries.
'''
Method                        	Description
clear()	                    Removes all the elements from the dictionary
copy()	                    Returns a copy of the dictionary
get()	                      Returns the value of the specified key
items()	                    Returns a list containing a tuple for each key value pair
keys()	                    Returns a list containing the dictionary's keys
pop()	                      Removes the element with the specified key
popitem()                 	Removes the last inserted key-value pair
setdefault()	              Returns the value of the specified key. If the key does not exist:
                            insert the key, with the specified value
update()	                  Updates the dictionary with the specified key-value pairs
values()                  	Returns a list of all the values in the dictionary'''
#Dictionary Items
'''
Dictionary items are ordered, changeable, and does not allow duplicates.
Dictionary items are presented in key:value pairs, and can be referred to by using the key name.'''
#Example
#Print the "brand" value of the dictionary:
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])'''

#Ordered or Unordered?
'''
As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.'''

#Changeable
#Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
'''
Duplicates Not Allowed
Dictionaries cannot have two items with the same key:'''
#Example
#Duplicate values will overwrite existing values:
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)'''
#dictionary length
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(len(thisdict))'''
#dictionary itmes_ datatype
'''
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)'''

# dictinoary(datatype)
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))'''

#Accessing Items
#You can access the items of a dictionary by referring to its key name, inside square brackets:
#Example
#Get the value of the "model" key:
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]'''

#There is also a method called get() that will give you the same result:
'''
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
print(x)'''

#Get Keys
#The keys() method will return a list of all the keys in the dictionary.
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.keys()
print(x)'''
#Add a new item to the original dictionary, and see that the keys list gets updated as well:
'''
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x)                             #before the change
car["color"] = "white"
print(x)                 '''        #after the change
#GET ITEMS
#the items() method will return each item in a dictionary, as tuples in a list.
#Example
#Get a list of the key:value pairs
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.items()
print(x)'''
#Add a new item to the original dictionary, and see that the items list gets updated as well:
'''
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x)                            #before the change
car["color"] = "red"
print(x)                           ''' #after the change

#check if Key Exists
#To determine if a specified key is present in a dictionary use the in keyword:
#Example
#Check if "model" is present in the dictionary:
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")'''

#Python - Change Dictionary Items
#Change Values
'''
You can change the value of a specific item by referring to its key name:
Example
Change the "year" to 2018:'''
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)'''

#Update Dictionary
#Example
#Update the "year" of the car by using the update() method:
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)'''

#Python - Remove Dictionary Items
#Removing Items
'''
There are several methods to remove items from a dictionary:
Example
The pop() method removes the item with the specified key name:'''
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)'''

#Example
#The popitem() method removes the last inserted item
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)'''

#Example
#The del keyword removes the item with the specified key name:
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)'''

#Example
#The del keyword can also delete the dictionary completely:
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#del thisdict
print(thisdict)'''
                                     #this will cause an error because "thisdict" no longer exists.
#Example
#The clear() method empties the dictionary:
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)'''

#Python Dictionary setdefault() Method

#Example
#Get the value of the "model" item:
'''
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("model", "bronco")
print(x)'''

#Definition and Usage
'''
The setdefault() method returns the value of the item with the specified key.
If the key does not exist, insert the key, with the specified value, see example below'''
#Syntax
#dictionary.setdefault(keyname, value)
'''
If the key exist, this parameter has no effect.
If the key does not exist, this value becomes the key's value
Default value None'''
#Example
#Get the value of the "color" item, if the "color" item does not exist, insert "color" with the value "white":
'''
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("color", "white")
print(x)'''

#example
'''
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("ideal")
print(x)'''


#Python Dictionary fromkeys() Method
#Example
#Create a dictionary with 3 keys, all with the value 0:

x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)
'''
Definition and Usage
The fromkeys() method returns a dictionary with the specified keys and the specified value.

#Syntax
dict.fromkeys(keys, value)
Parameter Values
Parameter                 	Description
keys	                  Required. An iterable specifying the keys of the new dictionary
value	                   Optional. The value for all keys. Default value is None

#Example
Same example as above, but without specifying the value:'''

x = ('key1', 'key2', 'key3')
thisdict = dict.fromkeys(x)
print(thisdict)








