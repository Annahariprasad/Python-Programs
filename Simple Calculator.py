                                        #Welcome to Calculator

print('<--------Welcome to Calculator-------->')

while(True):
    list=['Addition','Subtraction','Multiplication','Divison','Exponation','Floor Division','Exit']
    print('''\n1.Add(+)\t2.Subtract(-)\t3.Multiplication(*)\t4.Division(/)\t
    5.Exponation(**)\t6.Floor Division(//)\t7.Exit''')

    op=int(input('\nPress Number from the above options: '))
    if op == 7:
        print('Thank you for visiting')
        exit(False)
    elif op>6:
        print('<----Invalid Option---->')
        print('Please Enter option from 1 to 7 only')
    else:
        print('\nAre you want to',list[op-1]+':')
        a = int(input('Enter 1st Number: '))
        b = int(input('Enter 2nd Number: '))
        if op==1:
            print(str(a),'+',str(b), '=', str(int(a)+int(b)))
        elif op==2:
            print(str(a), '-', str(b), '=', str(int(a) - int(b)))
        elif op==3:
            print(str(a), '*', str(b), '=', str(int(a) * int(b)))
        elif op==4:
            print(str(a) ,'/', str(b), '=', str(int(a) / int(b)))
        elif op==5:
            print(str(a), '**', str(b), '=', str(int(a) ** int(b)))
        elif op==6:
            print(str(a), '//', str(b), '=', str(int(a) // int(b)))



