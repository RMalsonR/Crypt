import random


def create_table(world):
    table = [i for i in range(1, len(world)+1)]
    print(table)
    random.seed(5)
    random.shuffle(table)
    print(table)
    return table


def encrypt(table, world):
    result = ''
    for i in range(len(world)):
        for idx, val in enumerate(table):
            if val == i+1:
                result += world[idx]
    return result


if __name__ == '__main__':
    world = input('Enter the world: ').upper()
    print('Encrypt:\n ', encrypt(create_table(world), world))
