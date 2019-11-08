import random


def create_table(word):
    table = [i for i in range(1, len(word) + 1)]
    print(table)
    random.seed(5)
    random.shuffle(table)
    print(table)
    return table


def encrypt(table, word):
    result = ''
    for i in range(len(word)):
        for idx, val in enumerate(table):
            if val == i+1:
                result += word[idx]
    return result


def decrypt(table, word):
    result = ''
    for val in table:
        result += word[val - 1]
    return result


if __name__ == '__main__':
    word = input('Enter the word: ').upper()
    table = create_table(word)
    print('Encrypt:\n ', encrypt(table, word))
    word_decrypt = input('Enter word, witch you get in encrypt: ').upper()
    print('Decrypt:\n ', decrypt(table, word_decrypt))
