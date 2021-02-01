#Welcome to the Order_Match Program
def check_order(*args):
    list = args
    for i in list:
        for j in sublist:
            if i==j:
                sublist.pop(0)
            else:
                break
    return sublist

sublist = [1,1,5]
print('1) [1,5,6,4,1,2,3,5]\n2) [1,5,6,5,1,2,3.6]')
option = int(input('Enter option : '))
if option == 1:
    a = check_order(1,5,6,4,1,2,3,5)
    if len(a) == 0:
        print('it\' Match')
        print('First-list is matched')
    else:
        print('it\'s Gone')
        print('First-list is not matched')
elif option == 2:
    a = check_order(1,5,6,5,1,2,3.6)
    if len(a)==0:
        print('it\' Match')
        print('Second-list is matched')
    else:
        print('it\'s Gone')
        print('Second-list is not matched')
else:
    print('Select option from 2 options only')