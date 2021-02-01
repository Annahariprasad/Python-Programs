                                        #Arrays

#First We import array Module
#We import array module and applied all

from array import *

#PRINTING THE ARRAY NUMBERS IN NORMAL WAY
a=array('i',[2,7,3,9,4,8,1])
print('This is array: ')
for i in a:
    print(i,end=' ')

print()
#PRINTING THE ARRAY NUMBERS IN ASCENDING ORDER
b=sorted(a)
print('This is sorted array in ascending order: ')
print(b)
b.reverse()
print('This is sorted array in descending order: ')
for i in b:
    print(i,end=' ')
print()
#FINDING THE NUMBER IN THE ARRAY
value=int(input('Enter a number you want to find in array: '))
for i in range(len(a)):
    if a[i]==value:
        print('Your Number ', a[i],'is present in','Index number: ',i,)
        break
    else:
        i+=1
else:
    print('Number is not found!')
