#Now we installed numpy package successfully in pycharm
from numpy import *

#Here We discussed some functions present in numpy package
print('This is array : ',end=' ')
arr=array([1,2,3,4,5,6])
print(arr)
print('This is Data type : ',arr.dtype)
print()
#This is linspace which divides the parts
print('This is linspace : ')
arr1=linspace(0,10,15)
print(arr1)
print()
#This is logspace which divides the parts into ratios
print('This is logspace : ')
arr2=logspace(0,10,15)
print(arr2)
print()
#This is arange which is same as range function but not a range function
print('This is arange : ')
arr3=arange(0,15,2)
arr4=list(range(0,15,2))
print(arr3)
print(arr4)
print()
#This is zeros which prints the zeros in floating numbers
print('This is zeros : ')
arr5=zeros(10)
print(arr5)
print()
#This is ones which prints the zeros in floating numbers
print('This is ones : ')
arr6=ones(10)
print(arr6)
print()
#Mathematical functions in numpy module
print('These are trignometry functions : ')
print(sin(45))
print()
print(cos(45))
print()
print(tan(45))
print()
#SquareRoot
print('Square Root of 5 : ',sqrt(25))
print()
#Adding the numbers
print('This is sum function : ')
a=array([1,2,3,4,5])
print('The sum of the five numbers is : ',sum(a))
print()
#We copy the array
print('This is Normal Copy : ')
b=array([2,6,8,4,9])
c=b #this is normal copy but here having a disadvantage two variables sharing the one array address
print(c,'Id is : ',id(c))
print(b,'Id is : ',id(b))
print()
#We have two types of copies
#This is Shallow Copy
#This is create new array of the same array
print('This is Shallow Copy : ')
d=array([2,5,8,1,3,6])
e=d.view()#This is shallow copy function i.e., view()
print(d,'Id is : ',id(d))#Here also present in one disadvantage
print(e,'Id is : ',id(e))#once we change first array values automatically change the values in second array
print()
#This is Deep Copy
#Here We doesn't have a disadvantage
print('This is Deep Copy : ')
e=d.copy()#This is Deep copy function i.e., copy()
d[2]=7
print(d,'Id is : ',id(d))
print(e,'Id is : ',id(e))
