class Cell:
    string = ""
    first_cell = ''
    second_cell = ''
    third_cell = ''
    fourth_cell = ''
    fifth_cell = ''
    sixth_cell = ''
    seventh_cell = ''
    eighth_cell = ''
    ninth_cell = ''

    def __init__(self, cell):
        self.string = cell
        self.first_cell = cell[0]
        self.second_cell = cell[1]
        self.third_cell = cell[2]
        self.fourth_cell = cell[3]
        self.fifth_cell = cell[4]
        self.sixth_cell = cell[5]
        self.seventh_cell = cell[6]
        self.eighth_cell = cell[7]
        self.ninth_cell = cell[8]

    def __str__(self):
        print(self.first_cell + self.second_cell + self.third_cell)
        print(self.fourth_cell + self.fifth_cell + self.sixth_cell)
        print(self.seventh_cell + self.eighth_cell + self.ninth_cell + '\n')
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
