try:
    file = open('New File.py','r')
    file.write('Hi This is read mode only')
    file.close()
except Exception as error:
    print('Hey, This is read mode only, We can\'t write')
    print('Error occured')
    print('Error Message : ',error)
