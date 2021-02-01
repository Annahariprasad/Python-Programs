text = input('Enter a String : ')
lst = text.split(' ')
count = 0
lst1 = []
for i in lst:
    for j in i:
        count+=1
    lst1.append(count)
    count = 0

a = max(lst1)
for i in range(len(lst1)):
    if a == lst1[i]:
        print(lst[i])
        break