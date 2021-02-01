#This is Grid Pattern
def grid():
    print('+----+----+')
    for i in range(4):
        print('|    |    |')
    print('+----+----+')
    for i in range(4):
        print('|    |    |')
    print('+----+----+')

list = ['+ - - - - + - - - - +','|         |         |']
def grid1():
    print(list[0])
    for i in range(4):
        print(list[1])
    print(list[0])
    for i in range(4):
        print(list[1])
    print(list[0])

grid1()

