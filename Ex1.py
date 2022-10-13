# Программа написана для 221 конфеты, потому что с 2021 очень долго бы пришлось играть)
# Для игры с любым количеством конфет надо поменять только одну цифру в алгоритме сложного бота
# При игре с легким и сложным ботом игрок ходит первым, потому что иначе сложного бота не победить
import random


def twoNicknames():
    players.append(input('Первый игрок, представьтесь, пожалуйста:'))
    players.append(input('Второй игрок, представьтесь, пожалуйста:'))


def oneNickname():
    name = input('Игрок, представьтесь, пожалуйста:')
    players.append(name)


def step():
    firstStep = random.randint(1, 2)
    match firstStep:
        case 1: count = 0
        case 2: count = 1
    print(f'{players[count]} ходит первым!')
    return count


def modeCheck():
    mode = int(input(
        'Выберите режим игры:\n 1-игра друг против друга\n 2-игра против легкого бота\n 3-игра против сложного бота\n:'))
    if 1 <= mode <= 3:
        return mode
    else:
        print('Неправильно указан режим!')
        mode = int(modeCheck())
        return mode


def playerHand(count):
    hand = int(input(
        f'{players[count%2]} ходит! Выберите, сколько конфет вы хотите взять(1...28):'))
    if 0 < hand < 29:
        return hand
    else:
        print('Неправильное количество конфет!')
        hand = int(playerHand(count))
        return hand


def amountCheck(amount):
    i = 0
# Цифра 8 - предельное количество по 28 конфет для цикла игры с общим запасом в 221 конфету
# Записана она сюда, чтобы не гонять цикл лишние разы
# Для игры с 2021 конфетой ограничение нужно поднять до 72

    while i < 8:
        if amount == i*28+1:
            return True
        else:
            i += 1
    if i == 8:
        return False


def takeTo28(amount):
    if amount < 29:
        return amount
    else:
        for i in range(1, 28):
            if (amount-i) % 28 == 1:
                return i


def PvP(count):
    amount = 221
    while amount > 0:
        print(f'В корзине осталось {amount} конфет.')
        hand = int(playerHand(count))
        amount -= hand
        if amount <= 0:
            return (f'{players[count%2]} победил!')
        count += 1


def easyBot():
    amount = 221
    while amount > 0:
        print(f'В корзине осталось {amount} конфет.')
        hand = int(playerHand(0))
        amount -= hand
        if amount <= 0:
            return (f'{players[0]} победил!')
        print(f'В корзине осталось {amount} конфет.')
        botHand = random.randint(1, 29)
        print(f'Легкий бот берет {botHand} конфет.')
        amount -= botHand
        if amount <= 0:
            return ('Легкий бот победил!')


def hardBot():
    amount = 221
    while amount > 0:
        print(f'В корзине осталось {amount} конфет.')
        hand = int(playerHand(0))
        amount -= hand
        if amount <= 0:
            return (f'{players[0]} победил!')
        print(f'В корзине осталось {amount} конфет.')
        if amount == 1:
            botHand = amount
        else:
            check = amountCheck(amount)
            match check:
                case True: botHand = random.randint(1, 29)
                case False: botHand = takeTo28(amount)
        print(f'Сложный бот берет {botHand} конфет.')
        amount -= botHand
        if amount <= 0:
            return ('Сложный бот победил!')


players = []

gamemode = int(modeCheck())

match gamemode:
    case 1: twoNicknames()
    case 2: oneNickname()
    case 3: oneNickname()

if gamemode == 1:
    count = step()

match gamemode:
    case 1: print(PvP(count))
    case 2: print(easyBot())
    case 3: print(hardBot())
