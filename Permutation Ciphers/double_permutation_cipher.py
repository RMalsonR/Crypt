def create_table(word):
    table = [['_' for i in range(4)] for i in range(4)]
    count = 0
    for i in range(len(table)):
        for j in range(len(table[i])):
            if count == len(word):
                break
            table[i][j] = word[count]
            count = count + 1
    return table


def create_encrypt_table(table, column, row):
    result = table
    col = column
    while col != [1, 2, 3, 4]:
        for i in range(len(col) - 1):
            for j in range(i+1, len(col)):
                if col[i] > col[j]:
                    col[i], col[j] = col[j], col[i]
                    for n in range(len(result)):
                        result[n][i], result[n][j] = result[n][j], result[n][i]
    r = row
    while r != [1, 2, 3, 4]:
        for i in range(len(r) - 1):
            for j in range(i+1, len(r)):
                if r[i] > r[j]:
                    r[i], r[j] = r[j], r[i]
                    for n in range(len(result)):
                        result[i][n], result[j][n] = result[j][n], result[i][n]
    return result


def encrypt(table):
    result = ''
    for j in range(len(table[0])):
        for i in table:
            result += i[j]
    return result


def create_decrypt_table(word):
    table = [['_' for i in range(4)] for i in range(4)]
    count = 0
    for i in range(len(table)):
        for j in range(len(table[i])):
            if count == len(word):
                break
            table[j][i] = word[count]
            count = count + 1
    return table


def decrypt(table, column, row):
    result = table
    r = [1, 2, 3, 4]
    while r != row:
        for i in range(len(r)):
            for j in range(len(r)):
                if r[i] == row[j]:
                    r[i], r[j] = r[j], r[i]
                    for n in range(len(result)):
                        result[i][n], result[j][n] = result[j][n], result[i][n]
    col = [1, 2, 3, 4]
    while col != column:
        for i in range(len(col)):
            for j in range(len(col)):
                if col[i] == column[j]:
                    col[i], col[j] = col[j], col[i]
                    for n in range(len(result)):
                        result[n][i], result[n][j] = result[n][j], result[n][i]
    result_str = ''
    for i in result:
        for j in i:
            result_str += j
    return result_str


# 4 1 3 2     3 1 4 2
if __name__ == '__main__':
    word = input('Enter the word: ').upper()
    key_column, column_decrypt = [], []
    key_row, row_decrypt = [], []
    print('Enter the column keys:')
    while True:
        i = input()
        if not i:
            break
        key_column.append(int(i))
        column_decrypt.append(int(i))
    print('Enter the row keys:')
    while True:
        i = input()
        if not i:
            break
        key_row.append(int(i))
        row_decrypt.append(int(i))
    table = create_table(word)
    encrypt_table = create_encrypt_table(table, key_column, key_row)
    print('Encrypt: ', encrypt(encrypt_table))
    word_decrypt = input('Enter the decrypt word: ').upper()
    print('Decrypt: ', decrypt(create_decrypt_table(word_decrypt), column_decrypt, row_decrypt))
