#Pyramid Pattern

def pyramid(n):
    for i in range(1,n+1):
        for j in range(1,n+1-i):
            print(' ',end='')
        for k in range(1,i+1):
            print(' #',end='')
        print()

print('NAME : ANNA HARIPRASAD')
print('REGD NO : 19X51A0503')
n = int(input('Enter number : '))
pyramid(n)
