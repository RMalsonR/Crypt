import random

ALPHABET = [chr(i).upper() for i in range(1072, 1104)]
ALPHABET.insert(5, 'Ё')


def generate_first_items(table, alphabet):
    table[0][0] = ' '
    for j in range(1, len(table[0])):
        table[0][j] = random.choice(alphabet)
        alphabet.remove(table[0][j])
        table[0][j] += random.choice(alphabet)
        alphabet.remove(table[0][j][1])
    for i in range(1, len(table)):
        table[i][0] = random.choice(alphabet)
        alphabet.remove(table[i][0])
        table[i][0] += random.choice(alphabet)
        alphabet.remove(table[i][0][1])
    return table


def create_table(key):
    table = [['-' for j in range(7)] for i in range(7)]
    alphabet = [x for x in ALPHABET if x not in key]
    alphabet_with_key = [*key, *alphabet]
    alphabet_for_generating = alphabet
    a_index = 0
    table = generate_first_items(table, alphabet_for_generating)
    for i in range(1, len(table)):
        if a_index >= len(alphabet_with_key):
            break
        for j in range(1, len(table[i])):
            if a_index >= len(alphabet_with_key):
                break
            table[i][j] = alphabet_with_key[a_index]
            a_index += 1
    print('Created table:')
    for i in table:
        print(i)
    return table


def encrypt(table, word):
    result = ''
    for let in word:
        for idx_i, val_i in enumerate(table):
            for idx_j, val_j in enumerate(table[idx_i]):
                if idx_i == 0 or idx_j == 0:
                    continue
                if val_j == let:
                    result += random.choice(table[idx_i][0]) + random.choice(table[0][idx_j])
    return result


def split_encrypted_word(word):
    result = []
    i = 0
    while i < len(word):
        result.append(word[i] + word[i+1])
        i += 2
    return result


def decrypt(table, split_word):
    result = ''
    idx_i = 0
    idx_j = 0
    for group in split_word:
        for let in group:
            for i in range(1, len(table)):
                if let in table[i][0]:
                    idx_i += i
                if let in table[0][i]:
                    idx_j += i
            if idx_j == 0:
                continue
            result += table[idx_i][idx_j]
            idx_i = 0
            idx_j = 0
    return result


if __name__ == '__main__':
    key = input('Enter the key: ').upper()
    key = sorted(set(key), key=key.index)
    word = input('Enter the word: ').upper()
    table = create_table(key)
    print('Encrypt: ', encrypt(table, word))
    print('Decrypt:')
    word_decrypt = input('Enter the word: ').upper()
    print('Result: ', decrypt(table, split_encrypted_word(word_decrypt)))
