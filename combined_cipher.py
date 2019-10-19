ALPHABET = [chr(i).upper() for i in range(1072, 1104)]
ALPHABET.insert(5, 'Ё')
REVERSED_INDEXES = {
    1: 9, 2: 8, 3: 7,
    4: 6, 5: 5, 6: 4,
    7: 3, 8: 2, 9: 1
}


def reverse_index(index):
    if index == 0:
        return index
    else:
        return REVERSED_INDEXES[index]


def normalize_index(index):
    if index == 0:
        return index
    else:
        for _key in REVERSED_INDEXES:
            if REVERSED_INDEXES[_key] == index:
                return _key


def create_table(_key):
    _table = [['-' for x in range(10)] for i in range(4)]
    for idx, val in enumerate(_key):
        _table[0][idx] = val
    alphabet = [i for i in ALPHABET if i not in _key]
    a_index = 0
    for i in range(1, len(_table)):
        if a_index >= len(alphabet):
            break
        for j in range(len(_table[i])):
            if a_index >= len(alphabet):
                break
            _table[i][j] = alphabet[a_index]
            a_index += 1
    return _table


def encrypt(table, word):
    result = ''
    for let in word:
        for idx_i, val_i in enumerate(table):
            for idx_j, val_j in enumerate(table[idx_i]):
                if val_j == let:
                    if idx_i == 0:
                        result += str(reverse_index(idx_j))
                    else:
                        result += str(idx_i)
                        result += str(reverse_index(idx_j))
    return result


def split_encrypted(word, key):
    result = []
    ln = len(key)
    i = 0
    while i < len(word):
        if int(word[i]) > 3:
            result.append(word[i])
        else:
            result.append(word[i] + word[i + 1])
            i += 1
        i += 1
    return result


def decrypt(table, split_word):
    result = ''
    for group in split_word:
        if len(group) == 1:
            result += table[0][normalize_index(int(group))]
        else:
            result += table[int(group[0])][normalize_index(int(group[1]))]
    return result


# 610276202919
if __name__ == '__main__':
    key = input('Enter the key: ').upper()
    key = sorted(set(key), key=key.index)
    word = input('Enter the word: ').upper()
    table = create_table(key)
    choose = int(input('Choose mod:\n\t[1] - Encrypt\n\t[2] - Decrypt'))
    if choose == 1:
        for idx, col in enumerate(table):
            for let in table[idx]:
                print(let + ' ', end=' ')
            print('\n')
        print(encrypt(table, word))
    elif choose == 2:
        for idx, col in enumerate(table):
            for let in table[idx]:
                print(let + ' ', end=' ')
            print('\n')
        print(decrypt(table, split_encrypted(word, key)))
    else:
        raise ValueError('Choose correct mod: 1 or 2')
