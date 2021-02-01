                             #if, else & elif Statements


age=int(input('Enter your age: '))

if age>18 and age<70:
    print('You are eligible to drive')
elif age<18:
    print('You are not eligible to drive')
elif age==18:
    print('We cannot decide virtually you have to come to our office')
else:
    print('We can\'t reach')