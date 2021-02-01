#Diamond Pattern

n = int(input('Enter number : '))

for i in range(1,n+1):
    for j in range(1,n+1-i):
        print(' ',end='')
    for k in range(1,i+1):
        print(' *',end='')
    print()

for i in range(n-1,0,-1):
    for j in range(1,n+1-i):
        print(' ',end='')
    for k in range(1,i+1):
        print(' *',end='')
    print()
