import random


def twoNicknames():
    players.append(input('Первый игрок, представьтесь, пожалуйста:'))
    players.append(input('Второй игрок, представьтесь, пожалуйста:'))


def firstStep():
    firstStep = random.randint(1, 2)
    match firstStep:
        case 1: count = 0
        case 2: count = 1
    print(f'{players[count]} ходит первым!')
    return count


def step():
    coor = list(
        map(int, input('Введите через пробел строку и столбец(0...2):').split()))
    if 0 <= coor[0] <= 2 and 0 <= coor[1] <= 2:
        if cell[coor[0]][coor[1]] == '-':
            return coor
        else:
            print('Эта клетка уже занята! Выберите другую!')
            coor = list(step())
            return coor
    else:
        print('Неверные координаты!')
        coor = list(step())
        return coor


def printCell(cell):
    print(f'{cell[0][0]}|{cell[0][1]}|{cell[0][2]}')
    print('_____')
    print(f'{cell[1][0]}|{cell[1][1]}|{cell[1][2]}')
    print('_____')
    print(f'{cell[2][0]}|{cell[2][1]}|{cell[2][2]}')


def winCheck(cell):
    if cell[0][0] == cell[0][1] == cell[0][2] != '-':
        return True
    elif cell[1][0] == cell[1][1] == cell[1][2] != '-':
        return True
    elif cell[2][0] == cell[2][1] == cell[2][2] != '-':
        return True
    elif cell[0][0] == cell[1][0] == cell[2][0] != '-':
        return True
    elif cell[0][1] == cell[1][1] == cell[2][1] != '-':
        return True
    elif cell[0][2] == cell[1][2] == cell[2][2] != '-':
        return True
    elif cell[0][0] == cell[1][1] == cell[2][2] != '-':
        return True
    elif cell[0][2] == cell[1][1] == cell[2][0] != '-':
        return True
    else:
        return False


def game(count):
    while winCheck(cell) == False:
        print(f'Ход игрока {players[count%2]}!')
        coor = step()
        cell[coor[0]][coor[1]] = moves[count % 2]
        printCell(cell)
        if winCheck(cell) == True:
            print(f'{players[count%2]} победил!')
        count += 1


players = []
twoNicknames()
count = firstStep()
if count == 0:
    moves = ['X', 'O']
else:
    moves = ['O', 'X']
cell = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
printCell(cell)
game(count)
