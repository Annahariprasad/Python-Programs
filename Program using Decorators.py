#Decorators

import math

def getInput(func_argument):
    def wrap_function():
        a = int(input('Enter 1st Number : '))
        b =int(input('Enter 2nd Number : '))
        func_argument(a,b)
    return wrap_function

@getInput
def cone_volume_area(r,h):
    def cone_volume(r,h):
        print('Volume of the cone is : ', math.pi*pow(r,2)*h/3)
    def surface_area(r, h):
        print('surface_area of the cone : ', math.pi * r * (r + math.sqrt(pow(r, 2) + pow(h, 2))))
    cone_volume(r,h)
    surface_area(r,h)

@getInput
def ArmStrong(first,second):
    print("The Armstrong Numbers in a given range : ")
    for num in range(first,second):
        temp=num
        order = len(str(num))
        sum=0
        while temp>0:
            digit=temp%10
            sum+=digit**order
            temp//=10
        if num==sum:
            print(sum,end=' ')
    print()

@getInput
def prime_numbers(first,second):
    print('Prime Numbers in a given range : ')
    for i in range(first,second):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i, end=' ')
    print()

@getInput
def EvenNumbers(first,second):
    print('Even Numbers in the given range : ')
    for i in range(first,second+1):
        if i % 2 == 0:
            print(i,end=' ')
    print()

@getInput
def OddNumbers(first,second):
    print('Odd Numbers in the given range : ')
    for i in range(first,second+1):
        if i % 2 != 0:
            print(i,end=' ')
    print()

print('<----Welcome---->')
while True:
    print('''\n1.Volume and Area of the cone \t 2.Armstrong Numbers 
3.Prime Numbers \t 4.Even Numbers \t 5.Odd Numbers \t 6.Exit''')
    opt = int(input('\nEnter what you want from the above options : '))
    if opt == 1:
        cone_volume_area()
    elif opt == 2:
        ArmStrong()
    elif opt == 3:
        prime_numbers()
    elif opt == 4:
        EvenNumbers()
    elif opt == 5:
        OddNumbers()
    elif opt == 6:
        break
    else:
        print('Invalid option')
        print('Enter option from 1 to 6 only\n')