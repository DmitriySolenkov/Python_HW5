import random

def modeCheck():
    mode= int(input(
    'Выберите режим игры:\n 1-игра друг против друга\n 2-игра против легкого бота\n 3-игра против сложного бота\n:'))
    if 1<=mode<=3:
        return mode
    else:
        print('Неправильно указан режим!')
        return int(modeCheck)

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
        for i in range(1, 29):
            if (amount-i) % 28 == 1:
                return i


def PvP():
    count = 1
    amount = 221
    while amount > 0:
        print(f'В корзине осталось {amount} конфет.')
        hand = int(playerHand(count))
        amount -= hand
        if amount <= 0:
            return (f'{players[count%2]} победил!')
        count += 1


def easyBot():
    count = 1
    amount = 221
    while amount > 0:
        print(f'В корзине осталось {amount} конфет.')
        hand = int(playerHand(count))
        amount -= hand
        if amount <= 0:
            return (f'{players[count%2]} победил!')
        print(f'В корзине осталось {amount} конфет.')
        botHand = random.randint(1, 29)
        print(f'Легкий бот берет {botHand} конфет.')
        amount -= botHand
        if amount <= 0:
            return ('Легкий бот победил!')


def hardBot():
    count = 1
    amount = 221
    while amount > 0:
        print(f'В корзине осталось {amount} конфет.')
        hand = int(playerHand(count))
        amount -= hand
        if amount <= 0:
            return (f'{players[count%2]} победил!')
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


players = ('Игрок №2', 'Игрок №1')

gamemode = modeCheck
print(gamemode)
if gamemode == 1:
    print(PvP())
if gamemode == 2:
    print(easyBot())
if gamemode == 3:
    print(hardBot())
