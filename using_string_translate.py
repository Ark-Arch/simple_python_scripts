import string


file = input('Enter in your file: ')

try:
    with open(file) as fhand:
        word_dict = dict()
        for line in fhand:
            line = line.lower().strip()
            line = line.translate(line.maketrans('','',string.punctuation))
            for word in line.split():
                word_dict[word] = word_dict.get(word, 0) + 1
except:
    print('File does not exist!')
    exit()

print(word_dict)