from masons_cipher import *

if __name__ == '__main__':
    dictionary = {
        'a': Cell('--+ *|  |'), 'b': Cell('--+ *|--+'),
        'c': Cell('  | *|--+'), 'd': Cell('+-+|*|| |'),
        'e': Cell('+-+|*|+-+'), 'f': Cell('| ||*|+-+'),
        'g': Cell('+--|* |  '), 'h': Cell('+--|* +--'),
        'i': Cell('|  |* +--'), 'j': Cell('--+  |  |'),
        'k': Cell('--+  |--+'), 'l': Cell('  |  |--+'),
        'm': Cell('+-+| || |'), 'n': Cell('+-+| |+-+'),
        'o': Cell('| || |+-+'), 'p': Cell('+--|  |  '),
        'q': Cell('+--|  +--'), 'r': Cell('|  |  +--'),
        's': Cell('   \*/ V '), 't': Cell(' / <*  \ '),
        'u': Cell(' ^ /*\   '), 'v': Cell(' \  *> / '),
        'w': Cell('   \ / V '), 'x': Cell(' / <   \ '),
        'y': Cell(' ^ / \   '), 'z': Cell(' \   > / '),
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
