                                            #Patterns

for i in range(4):
    for j in range(4):
        print('# ',end='')
    print()

print()

for i in range(4):
    for j in range(4):
        print('* ',end='')
    print()

print()

for i in range(4):
    for j in range(i+1):
        print('# ',end='')
    print()

print()

for i in range(4):
    for j in range(4):
        print(i+1,end=' ')
    print()

print()

for i in range(4):
    for j in range(4-i):
        print(i+1,end=' ')
    print()

print()

for i in range(4):
    for j in range(i+1):
        print(4-i,end=' ')
    print()

print()

for i in range(4):
    for j in range(i+1):
        print('A', end=' ')
    print()

print()

for i in range(4):
    for j in range(4-i):
        print('A',end=' ')
    print()

print()

str1='ABCD'
str2='PQR'
for i in range(4):
    print(str1[:i+1]+str2[i:])

print()

str3='1234'
for i in range(4):
    print(str3[i:])