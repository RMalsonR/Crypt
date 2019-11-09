ALPHABET = [chr(i).upper() for i in range(1072, 1104)]
ALPHABET.insert(5, 'Ё')


def find_repeat_symbols(key):
    repeated = {}
    for i in range(len(key)-1):
        count = 0
        for j in range(i+1, len(key)):
            if key[i] == key[j]:
                count = count + 1
                repeated[key[i]] = count
    return repeated


def create_key_idxes(key):
    result = [i for i in range(len(key))]
    alphabet = [i for i in ALPHABET if i in key]
    if len(alphabet)!= len(key):
        repeated = find_repeat_symbols(key)
        for i in repeated:
            idx = alphabet.index(i)
            for j in range(repeated[i]):
                alphabet.insert(idx, i)
    checker = []
    for idx_a, val_a in enumerate(alphabet):
        for idx, val in enumerate(key):
            if idx in checker:
                continue
            if val_a == val:
                result[idx] = idx_a+1
                checker.append(idx)
                break
    return result


def create_table(key, word):
    n = len(key)
    m = int(len(word)/len(key)) if len(word) % len(key) == 0 else int(len(word)/len(key)) + 1
    table = [['_' for i in range(n)] for i in range(m+2)]
    for idx, val in enumerate(key):
        table[0][idx] = val
    idxes = create_key_idxes(key)
    for idx, val in enumerate(idxes):
        table[1][idx] = val
    count = 0
    for i in range(2, len(table)):
        for j in range(len(table[i])):
            if count == len(word):
                break
            table[i][j] = word[count]
            count = count + 1
    for i in table:
        print(i)
    return table


def encrypt(table, word):
    result = ''
    for i in range(1, len(table[0])+1):
        for idx, val in enumerate(table[1]):
            if val == i:
                for j in range(2, len(table)):
                    result += table[j][idx]
    return result


def decrypt(table, word):
    result = ''
    for i in range(2, len(table)):
        for j in table[i]:
            result += j
    return result


if __name__ == '__main__':
    key = input('Enter the key: ').upper()
    word = input('Enter the word: ').upper().replace(' ', '_')
    table = create_table(key, word)
    print('Encrypt: ', encrypt(table, word))
    word_decrypt = input('Enter the decrypt word: ').upper()
    print('Decrypt: ', decrypt(table, word_decrypt))

