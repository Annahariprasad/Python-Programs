                                       #ArmStrong Number
def ArmStrong(lst):
    for num in lst:
        temp=num
        order = len(str(num))
        sum=0
        while temp>0:
            digit=temp%10
            sum+=digit**order
            temp//=10
        if num==sum:
            yield num

lst = list(range(1,1000))
print(list(ArmStrong(lst)))


