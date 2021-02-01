def count_char(text):
    count = 0
    for c in text:
        if (c==' '):
            continue
        count+=1
    return count

file_name = input('Enter a string : ')
file = open('NewFile.txt','w')
file.write(file_name)
file.close()

filename = 'NewFile.txt'
with open(filename) as f:
    text = f.read()

print('No of words in a text file : ',count_char(text))