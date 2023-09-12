#backspace character
#\n   \t

#a="twinkle twinkle little star\nhow i wonder what you are,\n\tup above  the world so high\n\tlike a dimond in the sky"
#print(a)

#different data types
#a=5
#print(type(a))

#looping through string  
'''
a="arooj"                        
for x in a:
   print(x)'''
   
'''
for x in "arooj":
       print(x)'''


# string length
'''
a="hello ,world"
print(len(a))'''

#check string
'''
a="helloworld"
print("world" in a )
print("world" not in a )'''

#string slicing
# -9-8-7-6-5-4-3-2-1 
a= 'Aroujzahra'                                         #left to right
 #  0123456789
 
#print(a[3:5])     # 5 se aik km values ay gi
#print(a[:])
#print(a[:6])
#print(a[6:])
#print(a[-4:-2])        # 2  se aik km
#print(a[-3:-2])       # 1  se aik km

#modify string(upper and lower case)
#print(a.upper())
#print(a.lower())


#remove whitespaces

#a=" arooj zahra   "
#print(a.strip())
#print(a.rstrip())                  #right
#print(a.lstrip())              #left



#replace string
'''
a="helloworld"
print(a.replace("h","y"))'''


# split string
'''
a="helloworld"
print(a.split("o"))'''


# string concatenation
'''
b="pakistan is "
c="an under-developed country."
print(b+c)'''


#format string 
#example 1
'''
age=36
a="i'm john and i am {} year old."
print(a.format(age))'''

# example 2
'''
a=209
b=170
c=68.5
a="he price of petrol has been increased upto {}rs.\nor oil and electricity upto {} and {}rs.\n\t hats of the current governemnt"
print(a.format(a,b,c))'''

#example 3
'''
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))'''


# string concatenation

#Example 1
'''
a = "Hello "
b = "World"
c = a + b
print(c)'''

#Example 2
#To add a space between them, add a " ":
'''
a = "Hello"
b = "World"
c = a +" " + b
print(c)'''







