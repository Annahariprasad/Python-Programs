     #while loop executes when the condition is True

i=0
print("Numbers from 0 to 5: ")
while i<=5:
    print(i,end=' ')
    i+=1 #Incrementing by 1

#Printing the even numbers by using while loop
a=0
print("\nEven Numbers: ")
while a<=20:
    print(a,end=',')
    a+=2

#Printing the odd numbers by using while loop
b=0
print("\nOdd Numbers: ")
while b<=20:
    print(b,end=',')
    b+=3

#Break Statement is used to stop the loop
c=0
print('\nBreak the loop when c is 12: ')
while c<=20:
    print(c,end=',')
    if c==12:
        break
    c+=2

#Continue Statement is used to skip the loop
d=0
print('\nContinue the even numbers to skipping the 12 number: ')
while d<=20:
    d += 2
    if d==12:
        continue
    print(d, end=',')

e=0
print('\nThese Numbers does not divisible by 3 or 5: ')
while e<50:
    e = e + 1
    if e%3==0 or e%5==0:
        continue
    print(e,end=',')

