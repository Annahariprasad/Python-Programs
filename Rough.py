#14.Given rows of text, write it in the form of columns.

'''str = list(input('Enter a string : '))
for i in str:
    print(i)
'''

#16. Write program which performs the following operations on list’s. Don’t use built-in
#functions.
'''
a) Updating elements of a list
b) Concatenation of list’s
c) Check for member in the list
d) Insert into the list
e) Sum the elements of the list
f) Push and pop element of list
g) Sorting of list
h) Finding biggest and smallest elements in the list
i) Finding common elements in the list
'''
def count(l):
    cout=0
    for i in l: cout+=1
    return cout

def up_list(l,pos,ele):
   if pos>count(l):  return 'Out of index'
   else: l[pos-1] = ele
   return l

def constr(l1,l2):
    return l1+l2

def check(l,ele):
    if ele in l1: return 'Element is found in a list'
    else : return 'Element is not found in a list'

def insEle(l,pos,ele):
    if pos>=count(l)+1: return 'out of index'
    if pos>count(l)-1: return l[:-1]+[ele]+[l[-1]]
    else:
        a = l[pos-1:]
        l = l[:pos]
        l[pos-1]=ele
        l += a
    return l
        
def sumElem(l):
    s = 0
    for i in l:
        s+=i
    return s

def pushElem(l,ele):
    l+=[ele]
    return l

def popElem(l):
    print('popped element : ',l[-1])
    l = l[:-1]
    return l

def sortElem(l):
    for i in range(count(l)-1):
        if l[i]>l[i+1]:
            (l[i],l[i+1]) = (l[i+1],l[i])
    return l

def bigElem(l):
    big = l[0]
    for i in range(count(l)-1):
        if l[i]>=big:
            big = l[i]
    return big

def smallElem(l):
    small = l[0]
    for i in range(1,count(l)-1):
        if l[i]<small:
            small = l[i]
    return small

def comElem(l):
    a = []
    for i in range(count(l)-1):
        for j in range(i+1,count(l)-1):
            if l[i]==l[j]:
                if l[i] not in a: a += [l[i]]
    return a
    
        
            

l1 = [1,2,0,3,1,2,5,0,6]
l2 = [7,8,9,4,1,2]
print(l1)
#print('Count is : ',count(l1))
#print('List1 : ',l1,'\nList2 : ',l2)
#print('------------------------------')
#print('Updated List1 : ',up_list(l1,2,7),'\n')
#print('Concatenation List1 and List2 : ',constr(l1,l2),'\n')
#print('Check member in a List1 : ',check(l1,8),'\n')
for i in range(1,count(l1)+1):
    print('Insert element in a List1 : ',insEle(l1,i,15),'\n')
#print('Sum of List1 : ',sumElem(l1),'\n')
#print('Push element into the List1 : ',pushElem(l1,15),'\n')
#print('List1 : ',popElem(l1),'\n')
#print('List1 : ',l1,'\n')
#print('Sorted list1 : ',sortElem(l1),'\n')
#print('Biggest element of list2 : ',bigElem(l2),'\n')
#print('Smallest element of list1 : ',smallElem(l1),'\n')
print('Common elements of list1 : ',comElem(l1))
