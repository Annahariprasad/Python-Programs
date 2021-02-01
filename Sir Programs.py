#Square Root
'''
a = int(input('Enter number : '))
b = a**0.5
print('Square root of ',a,' : ',b)
'''

#Area of a Traingle
'''
a = int(input('Enter a value : '))
b = int(input('Enter b value : '))
c = 0.5*a*b
print('Area of a Traingle : ',c)
'''

#Quadratic Equation
'''
import math
a = int(input('Enter a value : '))
b = int(input('Enter b value : '))
c = int(input('Enter c value : '))
q = (-b + math.sqrt(b**2 - 4*a*c))/2*a
q1 = (-b - math.sqrt(b**2 - 4*a*c))/2*a
print('Values is : ',q,',',q1)
'''

#Swap Two Numbers
a = int(input('Enter a value : '))
b = int(input('Enter b value : '))
print('Before Swapping : a = ',a,'b = ',b)
(a,b) = (b,a)
print('After Swapping : a = ',a,'b = ',b)