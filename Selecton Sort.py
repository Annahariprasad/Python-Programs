#Selection Sort :

print('\t\tWELCOME TO SELECTION SORT\t\t')
n = int(input('Enter number : '))
a = []
for i in range(n):
    print('Enter a[',i,'] element : ',end="")
    x = int(input())
    a.append(x)

print('Before Sorting : ',end=" ")
for i in range(n):
    print(a[i],end=" ")

for i in range(n-1):
    min = i
    for j in range(i+1,n):
        if a[min] > a[j]:
            (a[min],a[j]) = (a[j],a[min])
        else:
            min = j
print()
print('After Sorting : ',end=" ")
for i in range(n):
    print(a[i],end=" ")