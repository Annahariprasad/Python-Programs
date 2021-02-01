from numpy import *

arr1=array([2,4,5,6,3])

for i in range(5):
    print (arr1[i]+5,end=' ')

print()

mx=0
for i in range(4):
    if arr1[i]>arr1[i+1] and arr1[i]>mx:
        mx=a[i]
    elif arr1[i+1]>mx:
        mx=arr1[i+1]

print('Maximum value is : ',mx)
