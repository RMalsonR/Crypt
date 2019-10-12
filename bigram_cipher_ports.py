from itertools import count as count_from

LANGUAGE = {
    'А': 0, 'Б': 1, 'В': 2, 'Г': 3,
    'Д': 4, 'Е': 5, 'Ж': 6, 'З': 7,
    'И': 8, 'К': 9, 'Л': 10, 'М': 11,
    'Н': 12, 'О': 13, 'П': 14, 'Р': 15,
    'С': 16, 'Т': 17, 'У': 18, 'Ф': 19,
    'Х': 20, 'Ц': 21, 'Ч': 22, 'Ш': 23,
    'Щ': 24, 'Ъ': 25, 'Ы': 26, 'Ь': 27,
    'Э': 28, 'Ю': 29, 'Я': 30,
}


def str_to_append(_str):
    if len(_str) == 1:
        return '00' + _str
    if len(_str) == 2:
        return '0' + _str
    if len(_str) == 3:
        return _str


def build_array():
    count = count_from(1)
    array = [[next(count) for i in range(1, 32)] for i in range(0, 31)]
    for i in range(len(array)):
        for j in range(len(array[i])):
            array[i][j] = str_to_append(str(array[i][j]))
    return array


def combine_word(_word):
    result = []
    intermediate = ''
    for i in range(len(_word)):
        if len(_word) % 2 != 0 and i + 1 == len(_word):
            intermediate += _word[i] + 'Я'
            result.append(intermediate)
            break
        intermediate += _word[i]
        if ((i + 1) % 2) == 0:
            result.append(intermediate)
            intermediate = ''
    return result


def encrypt(combined, table):
    result = ''
    for letters in combined:
        result += table[LANGUAGE[letters[0]]][LANGUAGE[letters[1]]] + ' '
    return result


def decrypt(cipher, table):
    result = ''
    find_str = cipher.split(' ')
    for find_value in find_str:
        for i, value_i in enumerate(table):
            for j, value_j in enumerate(value_i):
                if find_value == value_j:
                    for letter in LANGUAGE:
                        if LANGUAGE[letter] == i: result += letter
                        if LANGUAGE[letter] == j: result += letter
    return result


if __name__ == '__main__':
    print('Enter the word')
    _word = input()
    _word = _word.upper()
    _word = _word.replace('Ё', 'Е')
    _word = _word.replace('Й', 'И')
    print('Encrypt:')
    table = build_array()
    combined_word = combine_word(_word)
    print(encrypt(combined_word, table))
    print('Decrypt:')
    print('Enter the cipher:')
    cipher = input()
    print(decrypt(cipher, table))
