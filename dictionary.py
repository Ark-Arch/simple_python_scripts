file = input('Enter in your file: ')
count_comma = 0
words_dict = dict()
try:
    with open(file) as fhand:
        for line in fhand:
            line = line.replace(',','').strip()
            words = line.split()
            for word in words:
                if word not in words_dict:
                    words_dict[word] = ''
                

except:
    print('the file you want to read into does not exist')
    exit()

print(len(words_dict))