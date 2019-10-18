from re import findall

ALPHA = tuple("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ 1234567890")
MATRIX_LENGTH = 3
MATRIX_MOD = len(ALPHA)
MATRIX_SQUARE = MATRIX_LENGTH * MATRIX_LENGTH


# Проверка условий на ошибки
def checkErrors(key):
    if len(key) != MATRIX_SQUARE:
        return "Error: len(key) != %d" % MATRIX_SQUARE
    elif not getDeter(sliceto(key)):
        return "Error: det(Key) = 0"
    elif not getDeter(sliceto(key)) % MATRIX_MOD:
        return "Error: det(Key) mod len(alpha) = 0"
    else:
        return None


# Регулярное выражение - 3 символа сообщения
def regular(text):
    template = r".{%d}" % MATRIX_LENGTH
    return findall(template, text)


# Кодирование символов в матрице
def encode(matrix):
    for x in range(len(matrix)):
        for y in range(MATRIX_LENGTH):
            matrix[x][y] = ALPHA.index(matrix[x][y])
    return matrix


# Декодирование чисел в матрице + шифрование/расшифрование
def decode(matrixM, matrixK, message=""):
    matrixF = []
    for z in range(len(matrixM)):
        temp = [0 for _ in range(MATRIX_LENGTH)]
        for x in range(MATRIX_LENGTH):
            for y in range(MATRIX_LENGTH):
                temp[x] += matrixK[x][y] * matrixM[z][y]
            temp[x] = ALPHA[temp[x] % MATRIX_MOD]
        matrixF.append(temp)
    for string in matrixF:
        message += "".join(string)
    return message


# Создаёт матрицу по три символа
def sliceto(text):
    matrix = []
    for three in regular(text):
        matrix.append(list(three))
    return encode(matrix)


# Нахождение обратного определителя матрицы
def iDet(det):
    for num in range(MATRIX_MOD):
        if num * det % MATRIX_MOD == 1:
            return num


# Алгебраические дополнения
def algebratic(x, y, det):
    matrix = sliceto(mainKey)
    matrix.remove(matrix[x])
    for z in range(2):
        matrix[z].remove(matrix[z][y])
    det2x2 = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    return (pow(-1, x + y) * det2x2 * iDet(det)) % MATRIX_MOD


# Получение определителя матрицы
def getDeter(matrix):
    return \
        (matrix[0][0] * matrix[1][1] * matrix[2][2]) + \
        (matrix[0][1] * matrix[1][2] * matrix[2][0]) + \
        (matrix[1][0] * matrix[2][1] * matrix[0][2]) - \
        (matrix[0][2] * matrix[1][1] * matrix[2][0]) - \
        (matrix[0][1] * matrix[1][0] * matrix[2][2]) - \
        (matrix[1][2] * matrix[2][1] * matrix[0][0])


# Получение алгебраических дополнений
def getAlgbr(det, index=0):
    algbrs = [0 for _ in range(MATRIX_SQUARE)]
    for string in range(MATRIX_LENGTH):
        for column in range(MATRIX_LENGTH):
            algbrs[index] = algebratic(string, column, det)
            index += 1
    return algbrs


# Получение обратной матрицы
def getIMatr(algbr):
    return [
        [algbr[0], algbr[3], algbr[6]],
        [algbr[1], algbr[4], algbr[7]],
        [algbr[2], algbr[5], algbr[8]]
    ]


cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
if cryptMode not in ['E', 'D']:
    print("Error: mode is not Found")
    raise SystemExit

startMessage = input("Write the message: ").upper()
mainKey = input("Write the key: ").upper()

if checkErrors(mainKey):
    print(checkErrors(mainKey))
    raise SystemExit

for symbol in startMessage:
    if symbol not in ALPHA:
        startMessage = startMessage.replace(symbol, '')

while len(startMessage) % MATRIX_LENGTH != 0:
    startMessage += startMessage[-1]


# Основная функция
def encryptDecrypt(mode, message, key):
    MatrixMessage, MatrixKey = sliceto(message), sliceto(key)
    if mode == 'E':
        final = decode(MatrixMessage, MatrixKey)
    else:
        algbr = getAlgbr(getDeter(MatrixKey))
        final = decode(MatrixMessage, getIMatr(algbr))
    return final


print("Final message:", encryptDecrypt(cryptMode, startMessage, mainKey))