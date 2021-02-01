                      #For Loops
'''
names=['Hari','Deepak','Pavan','Tharun','Bablu']
for name in names:
    print(name) #Printing the names of the names list by using 'for; loop
'''

'''
for x in 'Annahari':
    print(x) #Printing the every single letter in 'Annahari' String
'''

'''
fruits=['Apple','Banana','Grapes','Orange','Pineapple']
for fruit in fruits:
    print(fruit)
    if fruit=='Grapes':
        break
'''
'''
fruits=['Apple','Banana','Grapes','Orange','Pineapple']
for fruit in fruits:
    if fruit=='Grapes':
        break
    print(fruit)
'''

'''
names=['Deepak','Tharun','Pavan','Hari','Bablu']
for name in names:
    if name=='Tharun':
        continue
    print(name)
'''

'''
for x in range(10):
    print('Number is ' + str(x))
'''

'''
print('Numbers from 4 to 19')
for x in range(4,20):
    print(x,end=',')
'''

'''
print('     Even Numbers from 0 to 30:')
for x in range(0,30,2):
    print(x,end=',')
'''

'''
print('Odd Numbers from 0 to 30:')
for x in range(0,30,3):
    print(x,end=',')
'''

'''
Mobiles=['\nOneplus','Samsung','Redmi','Realme','Moto','Infinix']
for company in Mobiles:
    print(company,end=',')
else:
    print('\n\t\t\"Companies is Finish\"')
'''


'''
Laptops=['Asus','HP','Dell','Apple','Lenovo','MI','Honour']
Rating=['5 Star']
for x in Laptops:
    for y in Rating:
        print(str(x) + ' have ' + str(y) + ' Company Laptops')
'''

for x in range(6):
    pass #We want to keep the loop empty use this keyword "pass"

#Odd Numbers in a range
n = int(input('Enter Range : '))
nums = range(1,n+1)
odd = list(filter(lambda x : (x%2 !=0), nums))
print(odd)
#Even Numbers in a range
even = list(filter(lambda x: (x%2 == 0),nums))
print(even)
