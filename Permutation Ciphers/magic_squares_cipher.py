import numpy as np


def create_table():
    N = 4
    magic_square = np.zeros((N, N), dtype=int)
    n = 0
    i, j = 0, N // 2
    while n <= N ** 2:
        magic_square[i, j] = n
        n += 1
        newi, newj = (i - 1) % N, (j + 1) % N
        if magic_square[newi, newj]:
            i += 1
        else:
            i, j = newi, newj
    return magic_square


def create_intermediate_table(table, word):
    result = [['.' for i in range(4)] for i in range(4)]
    for idx, val in enumerate(word):
        for idx_i, val_i in enumerate(table):
            for idx_j, val_j in enumerate(val_i):
                if val_j == idx+1:
                    result[idx_i][idx_j] = val
    return result


def encrypt(table):
    result = ''
    for i in table:
        for j in i:
            result += j
    return result


def decrypt(table_intermediate, table, word):
    result = ''
    count = 1
    while count <= len(word):
        for idx_i, val_i in enumerate(table):
            for idx_j, val_j in enumerate(val_i):
                if count == val_j:
                    result += intermediate_table[idx_i][idx_j]
                    count += 1
    return result


if __name__ == '__main__':
    word = input('Enter the word: ').upper().replace(' ', '.')
    table = create_table()
    print(table)
    intermediate_table = create_intermediate_table(table, word)
    print('Encrypt: ', encrypt(intermediate_table))
    word_decrypt = input('Enter the decrypt word: ').upper()
    print('Decrypt: ', decrypt(intermediate_table, table, word))
