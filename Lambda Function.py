list=['hey this is sai','I am in mumbai','i am learning python from letsupgrade']
capitalize = lambda list : list.title()

caps = map(capitalize,list)
caps_list = []
for i in caps:
    caps_list.append(i)

print(caps_list)
