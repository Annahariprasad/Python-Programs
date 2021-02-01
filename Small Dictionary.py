while(True):
    print('\n1.accidial', '2.Agender', '3.Airball', '4.Automagically', '5.Awesomesauce', '6.Exit')
    meanings={
         'accidial':'dial someone\'s number on phone accidentally',
         'agender':'people do not identify as male or female',
         'airball':'completely miss the basket, rim, and backboard with a shot',
         'automagically':'in a way that seems magical, especially by computer',
         'awesomesauce':'extremely good; excellent'
          }
    print('Please select the above five numbers only')
    user=int(input("Enter you want to know the meaning of a word of a number : "))
    if user==1:
        print('Meaning of a word is : ', meanings['accidial'])
    elif user==2:
        print('Meaning of a word is : ', meanings['agender'])
    elif user==3:
        print('Meaning of a word is : ', meanings['airball'])
    elif user==4:
        print('Meaning of a word is : ', meanings['automagically'])
    elif user==5:
        print('Meaning of a word is : ', meanings['awesomesauce'])
    elif user==6:
        exit(False)
    else:
        print("Please select from 1 to 5 only")