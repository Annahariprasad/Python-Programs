def ack(m,n):
    if(m == 0):
        return n+1
    if(m > 0 and n == 0):
        return ack(m-1,1)
    return ack(m-1,ack(m,n-1))

print("Name : Anna Hariprasad")
print("Regno : 19X51A0503\n")
m = int(input("Enter the m value : "))
n = int(input("Enter the n value : "))
print(ack(m,n))
