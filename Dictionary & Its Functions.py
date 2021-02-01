                                            #Dictionary
                                    #Dictionary is Key-Value Pairs
laptops={
         'Annahari':'Asus Vivobook 14', #This is Laptops We are using now
         'Majahar':'HP CS3006',
         'Gnaneswar':'HP Pavilion Gaming',
         'Sudheer':'Dell Insipirin'
        }
#This is Electronic Gadgets We are using now
devices={
         'Annahari':{'Mobile':'Honour 9 lite','Laptop':'Asus Vivobook','Earphones':'Oneplus Wireless Z'},
         'Majahar':{'Mobile':'Redmi Y1','Laptop':'HP CS3006','Earphones':'Touchtek Wireless'},
         'Gnaneswar':{'Mobile':'Realme Xt','Laptop':'HP Pavilion Gaming','Earphones':'Boat Earphones'},
         'Shabareesh':{'Mobile':'Realme 2 Pro','Laptop':'HP Core i5','Earphones':'Ptron Wireless'}
        }

print(type(laptops)) #Printing the type of variable and this is dictionary type

print(laptops) #Printing the laptops dictionary

print(laptops['Annahari'],end=", ") #Printing the dictionary with specific key
print(laptops['Majahar'],end=", ") #Printing the dictionary with specific key
print(laptops['Gnaneswar'],end=", ") #Printing the dictionary with specific key
print(laptops['Sudheer']) #Printing the dictionary with specific key

laptops['Adnan']='HP Gaming Laptop' #Adding the another key and it's value in the laptops dictionary
print(laptops) #Printing the laptops dictionary after adding the new key and it's value

del laptops['Adnan'] #Delete the specific key and it's value
print(laptops) #Printing the laptops dictionary after deleting the specific key and it's value

laptops=devices.copy() #Here we copying the devices dictionary into the laptops dictionary by using copy() Function
del devices['Annahari'] #Here we deleting the key value in the devices dictionary
print(devices) #Printing the devices dictionary
print(laptops) #Printing the laptops dictionary

print(laptops.get('Gnaneswar')) #Here We display the specific key value by using get() Function

print(laptops.update({'Finishing':'These are Electroic Devices we are using'}))#Here we Adding or Update the new key in the laptops dictionary
print(laptops)#Printing the laptops dictionary after update the new key and it's value

print(laptops.keys()) #Printing the keys only present in the laptops dictionary by using the key() Function
print(laptops.items()) #Printing the keys and it's value by using the items() Function