                               #Lists

print('Lists')
numbers=[2,5,8,6,9]
laptops=['asus','hp','dell','apple','mi','honour']

print(numbers)#Printing the Lists
print(laptops)#Printing the Lists

print('\nLength:')
print("List of Numbers is",len(numbers))#Printing the length of the lists
print("List of laptops is",len(laptops))#Printing the length of the lists

print('\nChanging:')
numbers[2]=3#Changing the value at the index
laptops[5]='avita'#Changing the value at the index

print(numbers) #Printing the Lists after changing the values
print(laptops) #Printing the Lists after changing the values

                            #Lists Functions
print('\n\"List Functions\"')
print('\nSorting:')
numbers.sort() #Sorting The list by using Sort() Function
laptops.sort() #Sorting The list by using Sort() Function
print(numbers)#Printing the sorting the list
print(laptops)#Printing the sorting the list

print('\nAppend:')
numbers.append(8)#Adding the value in the list at the end by using append() function
laptops.append('honour')#Adding the value in the list at the end by using append() function
print(numbers)#Printing the list after adding the value at the end
print(laptops)#Printing the list after adding the value at the end

print('\nPop:')
numbers.pop()#Remove the value in the list at the end by using pop() function
laptops.pop()#Remove the value in the list at the end by using pop() function
print(numbers)#Printing the list after removing the value at the end
print(laptops)#Printing the list after removing the value at the end

print('\nInsert:')
numbers.insert(2,34)#Inserting the value in the list at specific index
laptops.insert(3,'lenovo')#Inserting the value in the list at specific index
print(numbers)#Printing the list after adding the value at specific index
print(laptops)#Printing the list after adding the value at specific index

print('\nRemove:')
numbers.remove(34)#Remove the element at specific index
laptops.remove('lenovo')#Remove the element at specific index
print(numbers)#Printing the list after removing the value at specific index
print(laptops)#Printing the list after removing the value at specific index

                 #So many Built-in Functions are available in python