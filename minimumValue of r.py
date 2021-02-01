print("Name : Anna Hariprasad")
print("Regno : 19X51A0503\n")

n = int(input("Enter n value : "))
for r in range(n):
    if(n+r+1 <= (2**r)):
        print("The minimum value of r is : ",r)
        break
