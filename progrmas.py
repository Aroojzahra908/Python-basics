#logic opertaor
'''a=5
b=6
c=7
if(a<b)and(a<c):
  print(True)
else:
    print(False)  '''
'''
a=5
b=6
c=7
if(a>b)or(a<c):
  print(True)
else:
    print(False)  '''
'''
a=5
b=6
c=7
if not(a<b):
  print(True)
else:
    print(False)  '''
# find maximum number
'''
a=5
b=10
c=15
if a>b and a>c:
    print("max number=",a)
elif b>a and b>c:
    print("max number=",b)  
else:
    print ("max number=",c)  '''

# find the number is negative positive or zero
'''
a=int(input("enter a number:"))
if a>0:
    print("positive")
elif a<0:
    print("negative")
else:
    print ("zero")   
    '''
# using while loop
# print no 1 to 10
'''
i=1
while(i<=10):
    print(i)
    i=i+1''' 
# reverse order print natural number        
'''
i=10
while(i>=1):
    print(i)
    i=i-1    
'''
# for looop
'''

for i in range(1,10):                # step value
    print (i)  '''

#Write a program that inputs five integers. It finds and prints the largest and the smallest integer.
'''
n=int(input("enter the total element number is:"))
l1=list()
for i in range (n):
    number=int(input("enter the number:"))
    l1.append(number)
    Min=min(l1)
    Max=max(l1)
print ("maximun number is:",Max)   
print ("minimum number is:",Min) '''
'''
Write a program that inputs an integer and displays the sum of its digits. For example, the program should
display 9 if the user enters 135.'''
'''
i=int(input("enter number to find sum of digits:"))
sum=0
while(i>0):
    sum=sum+i%10
    i=i//10
print("sum of digits =",sum)'''


'''
i=int(input("enter no to check for armstrong"))
original=i
sum=0
while(i>0):
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
if original==sum:
    print("number is armstrong")    
else:
    print("number is not armstrong")    '''


