class Cell:
    string = ''

    def __init__(self, cell):
        self.string = cell

    def __str__(self):
        for let in self.string:
            print(let, end='')
        return self.string


def encrypt(_word, _dictionary):
    for letter in _word:
        _dictionary[letter].__str__()


def decrypt(_cells, _dictionary):
    result = ''
    for cell in _cells:
        for _word in _dictionary:
            if is_equal(_dictionary[_word].string, cell):
                result += _word
                break
    print(result)


def is_equal(_word, cell):
    return cell.string == _word


if __name__ == '__main__':
    dictionary = {
        'a': Cell('(V)'), 'b': Cell('(^)'),
        'c': Cell('(<)'), 'd': Cell('(>)'),
        'e': Cell('(X)'), 'f': Cell('(+)'),
        'g': Cell('(|)'), 'h': Cell('(-)'),
        'i': Cell('(\)'), 'j': Cell('(/)'),
        'k': Cell("('-)"), 'l': Cell("(-')"),
        'm': Cell('(,-)'), 'n': Cell('(-,)'),
        'o': Cell('(|-)'), 'p': Cell('(-|)'),
        'q': Cell("(-'-)"), 'r': Cell('(-,-)'),
        's': Cell('(\-)'), 't': Cell('(-\)'),
        'u': Cell('(-/)'), 'v': Cell('(/-)'),
        'w': Cell('(/|\)'), 'x': Cell('(Y)'),
        'y': Cell('(>-)'), 'z': Cell('(-<)'), ' ': Cell(' '),
    }
    print('Enter the word: ')
    word = input()
    print('Encrypt: ')
    encrypt(word, dictionary)
    print('Decrypt: ')
    print('Enter the cipher:')
    cells = []
    while True:
        cipher = input()
        if not cipher:
            break
        cells.append(Cell(cipher))
    decrypt(cells, dictionary)
