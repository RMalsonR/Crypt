class Cell:
    string = ""

    def __init__(self, cell):
        self.string = cell

    def __str__(self):
        print(self.string[0] + self.string[1] + self.string[2])
        print(self.string[3] + self.string[4] + self.string[5])
        print(self.string[6] + self.string[7] + self.string[8] + '\n')
        return self.string


def encrypt(word, dictionary):
    for letter in word:
        dictionary[letter].__str__()


def decrypt(cells, dictionary):
    result = ''
    for cell in cells:
        for word in dictionary:
            if is_equal(dictionary[word].string, cell):
                result += word
                break
    print(result)


def is_equal(word, cell):
    return cell.string == word
