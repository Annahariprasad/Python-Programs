                           #Sets

thisset={'Orange','Banana','Apple'}
print(type(thisset)) #Printing the type of the variable
print(thisset) #Printing the set

#sets are unordered and unindexed we can't access the elements by using index & Position
#So we can use 'for' loop for accessing the set elements
for x in thisset:
    print(x)

#Check the element is present or not in the set
print('Orange' in thisset)

#We cannot change the elements in the set
#We can add the new elements in the set by using add() Function
thisset.add('Cherry')
print(thisset)

#We can add more than one elements by using update() Function
thisset.update(['Pineapple','Pomegranate','Papayya'])
print(thisset)

#We can know the length of the set by using len() Function
print(len(thisset))

#We want to remove the element in the set by using remove() Function
thisset.remove('Papayya')
print(thisset)

#We want to remove the element by using discard() Function
thisset.discard('Cherry')
print(thisset)

thisset.pop()
print(thisset)

#We want to clear the all elements in the set by using clear() Function
thisset.clear()
print(thisset)

#We want to join the two sets by using union() Fucntion
set1={1,2,3}
set2={'a','b','c'}
set3=set1.union(set2)
print(set3)

