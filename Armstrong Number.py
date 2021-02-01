                                       #ArmStrong Number
for num in range(1042000,702648265):
    temp=num
    order = len(str(num))
    sum=0
    while temp>0:
        digit=temp%10
        sum+=digit**order
        temp//=10
    if num==sum:
        print("The First Armstrong Number in a given range : ",sum)
        break

