'''
print('This is numbers from 1 to 20: ')
for i in range(1,21):
    print(i, end=' ')
print()
print('This is even numbers from 1 to 20: ')
for i in range(1,20):
    if i%2==0:
        print(i,end=' ')
print()
print('This is odd numbers from 1 to 20: ')
for i in range(1,20):
    if not i%2==0:
        print(i,end=' ')
print()

print('This is prime numbers from 1 to 20:')
for i in range(1,20):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end=' ')

'''

                                    #PRIME NUMBERS


'''
This program check the number is prime or not
'''
def prime(given_number):
    '''
    This function check the number is prime or not
    '''
    for i in range(2,given_number):
        if given_number%i==0:
            return 'Not Prime Number'
            break
        else:
            return 'Prime number'
            break

a = prime(6)
print(a)
'''
print('Prime Numbers : ',end=' ')
pr = list(filter(prime,range(2500)))
print(pr)
'''
