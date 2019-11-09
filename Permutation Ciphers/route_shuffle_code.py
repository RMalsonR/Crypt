def create_table(n, m, word):
    table = [['_' for i in range(m)] for i in range(n)]
    count = 0
    for i in range(len(table)):
        for j in range(len(table[i])):
            if count == len(word):
                break
            table[i][j] = word[count]
            count = count + 1
    return table


def create_table_decrypt(n, m, word):
    table = [['_' for i in range(m)] for i in range(n)]
    count = 0
    for j in range(len(table[0])):
        for idx, val in enumerate(table):
            if count == len(word):
                break
            table[idx][j] = word[count]
            count = count + 1
    return table


def encrypt(table):
    result = ''
    for j in range(len(table[0])):
        for i in table:
            result += i[j]
    return result


def decrypt(table):
    result = ''
    for i in table:
        for j in i:
            result += j
    return result


if __name__ == '__main__':
    word = input('Enter the word: ').upper().replace(' ', '_')
    key = int(input('Enter the matrix size, like 67: '))
    table = create_table(int(key / 10), key % 10, word)
    print(table)
    print('Encrypt: ', encrypt(table))
    word_decrypt = input('Enter the decrypt word: ').upper()
    table = create_table_decrypt(int(key / 10), key % 10, word_decrypt)
    print('Decrypt: ', decrypt(table))
