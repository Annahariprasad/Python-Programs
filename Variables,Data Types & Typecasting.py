#These are Variables

a=57  #Integer datatype
b=86.7 #Float datatype
c="Hello World!" #string datatype
d=3+5j #complex datatype
e='Hi I am Python' #string datatype
print(a+b) #Adding two numbers
print(str(a)+str(b)) #Combining two numbers with String Format
print(a+d) #Adding integer with complex number
print(c+', '+e) #Combining two strings with adding coma
#Here We can't Combine the string with numeric data types
print(type(a)) #print the variable datatype --> (Integer)
print(type(b)) #print the variable datatype --> (Float)
print(type(c)) #print the variable datatype --> (String)
print(type(d)) #print the variable datatype --> (Complex)
print(float(a)+b) #Here we change integer datatype into float datatype and add with float number
#Here can't convert complex into other any datatype
print(str(a)+' '+c+' '+e) #Here we convert integer into string datatype
print(5*c) #Here we print the string five times by multiplying with five integer
