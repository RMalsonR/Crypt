TABLE_1 = [
    [1, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 0]
]
TABLE_2 = [
    [0, 1, 0, 1],
    [0, 0, 0, 0],
    [1, 0, 1, 0],
    [0, 0, 0, 0]
]
TABLE_3 = [
    [0, 0, 0, 0],
    [1, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 1, 0, 1]
]
TABLE_4 = [
    [0, 0, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 0],
    [1, 0, 1, 0]
]


def create_table(word):
    inter = pow(len(word), 0.5)
    n = inter if inter.is_integer() else int(inter+1)
    if n % 2 == 0:
        pass
    else:
        n += 1
    table = [['_' for i in range(n)] for i in range(n)]
    count_word = 0
    while count_word < len(word):
        if count_word < n*n / 4:
            supp_table = TABLE_1
        elif n*n / 4 <= count_word < n*n / 2:
            supp_table = TABLE_2
        elif n*n / 2 <= count_word < n*n*0.75:
            supp_table = TABLE_3
        else: supp_table = TABLE_4
        for idx_i, val_i in enumerate(table):
            for idx_j, val_j in enumerate(val_i):
                if count_word >= len(word):
                    break
                if supp_table[idx_i][idx_j]:
                    table[idx_i][idx_j] = word[count_word]
                    count_word += 1
    return table


def encrypt(table):
    result = ''
    for j in range(len(table[0])):
        for i in table:
            result += i[j]
    return result


def decrypt(table, word):
    result = ''
    n = len(table)
    count_word = 0
    while count_word < len(word):
        if count_word < n*n / 4:
            supp_table = TABLE_1
        elif n*n / 4 <= count_word < n*n / 2:
            supp_table = TABLE_2
        elif n*n / 2 <= count_word < n*n*0.75:
            supp_table = TABLE_3
        else: supp_table = TABLE_4
        for idx_i, val_i in enumerate(table):
            for idx_j, val_j in enumerate(val_i):
                if count_word >= len(word):
                    break
                if supp_table[idx_i][idx_j]:
                    result += table[idx_i][idx_j]
                    count_word += 1
    return result


if __name__ == '__main__':
    word = input('Enter the word: ').upper().replace(' ', '+')
    table = create_table(word)
    print('Encrypt: ', encrypt(table))
    word_decrypt = input('Enter the decrypt word: ').upper()
    print('Decrypt: ', decrypt(table, word_decrypt))
