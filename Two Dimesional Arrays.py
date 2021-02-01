from numpy import *

print('Two Dimensional array: ')
a=array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
        ])
print(a)

#Printing the dimensional of the array
print('The dimensional of array is : ',a.ndim)

#Printing the dimensions of the array
print('The dimensions(Rows & Columns) of array is: ',a.shape)

#Printing the array like one dimensional array
print('The two dimensional array in one dimensional is : ',a.flatten())#flatten(self)

#Printing the array to our wish like changing the dimensions
b=a.flatten()
print('We changing the array to our convenience : ')
print(b.reshape(4,3)) #reshape(rows,columns)

#Printing the array to divide and set dimensions to the given array
print('Two arrays with different dimenions : ')
print(a.reshape(2,3,2))