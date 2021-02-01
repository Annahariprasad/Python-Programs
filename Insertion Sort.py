#Insertion Sort :

print('\t\tWELCOME TO INSERTION SORT\t\t')
n =int(input('Enter number : '))
a = []
for i in range(n):
    print('Enter a[',i,'] element : ',end='')
    x = int(input())
    a.append(x)

print('Before Sorting : ',end='')
for i in range(n):
    print(a[i],end=' ')

for i in range(1,n):
    key = a[i]
    j=i-1
    while j>=0 and a[j]>key:
        (a[j],a[j+1]) = (a[j+1],a[j])
        j=j-1

print()
print('After Sorting : ',end='')
for i in range(n):
    print(a[i],end=' ')