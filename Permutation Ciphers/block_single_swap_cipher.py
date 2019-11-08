import random, re


def create_table():
    table = [i for i in range(1, 4)]
    print(table)
    random.seed(3)
    random.shuffle(table)
    print(table)
    return table


def split_word(word):
    while len(word) % 3 != 0:
        word += 'Ъ'
    return re.findall('...', word)


def encrypt(table, splitted_word):
    result = ''
    for block in splitted_word:
        for idx_block in range(len(block)):
            for idx, val in enumerate(table):
                if val == idx_block + 1:
                    result += block[idx]
    return result


def decrypt(table, word):
    result = ''
    for block in word:
        for val in table:
            result += block[val - 1]
    return result


if __name__ == '__main__':
    word = input('Enter the word: ').upper()
    table = create_table()
    splitted_word = split_word(word)
    print('Encrypt: ', encrypt(table, splitted_word))
    word_decrypt = split_word(input('Enter word, witch you get in encrypt: ').upper())
    print('Decrypt: ', decrypt(table, word_decrypt))
