#TAKING INPUTS IN ARRAY

from array import *

a=array('i',[])
n=int(input('Enter how many values you want to insert: '))

for i in range(n):
    if i==0:
        print('Enter',i+1,'st index number: ')
        b = int(input())
        a.append(b)
    elif i==1:
        print('Enter',i+1,'nd index number: ')
        b = int(input())
        a.append(b)
    else:
        print('Enter',i+1,'th index number: ')
        b=int(input())
        a.append(b)

print(a)

#SEARCHING AN ELEMENT IN ARRAY
val=int(input('Enter number you want to search: '))
for i in range(n):
    if a[i]==val:
        print('Your element index number is: ',i)
        break
    else:
        i+=1
else:
    print('Your element is not found!')


'''
list=[]

n=int(input('Enter how many elements you want to insert: '))

for i in range(n):
    print('Enter',i+1,'index number: ')
    x=int(input())
    list.append(x)

print('List is: ',list)
'''