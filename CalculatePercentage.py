n = int(input('Enter how many subjects : '))
print()
sub,grad,cred = [],[],[]
grval = {'s':10,'a':9,'b':8,'c':7,'d':6,'e':5}
num, den = 0,0

for i in range(n):
    x = input('Enter subject name : ')
    sub.append(x)
    y = input('Enter grade : ')
    grad.append(y.lower())
    z = float(input('Enter credits : '))
    cred.append(z)
    print()

for i in range(n):
    num += (grval[grad[i]]*cred[i])
    den += cred[i]

print()
print('------------------------------------------------------------------------')
print('subjects                        grades                      credits')
for i in range(n):
    print('------------------------------------------------------------------------')
    print(sub[i],'                          ',grad[i],'                    ',cred[i])

print('\nYour percentage is ',(num/den)*10)
