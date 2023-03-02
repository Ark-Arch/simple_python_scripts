word = 'brontosaurus'

def crude_method(word):
    word_count = dict()
    for letter in word:
        if letter in word_count:
            word_count[letter] += 1
        else:
            word_count[letter] = 1
    print(word_count)


def get_method(word):
    word_count = dict()
    for letter in word:
        word_count[letter] = word_count.get(letter,0) + 1
    print(word_count)

print(crude_method(word))
print(get_method(word))