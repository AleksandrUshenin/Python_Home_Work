import random

def exercise2():
    bot = menu()
    user = random.randint(1, 3)
    do = True
    count = 400
    while do:
        if user == 1:
            user = 2
        else:
            user = 1

        if bot and user == 2:
            (do, count) = botUser(count)
        else:
            (do, count) = User(count, user)

        PrintConsole("count =", count)
    PrintConsole('{} игрок проиграл'.format(user))
    PrintConsole(count)

def botUser(count):
    sel = 28
    while True:
        res = count % sel

        if res == 0 and count - res != 0:
            break
        if sel != 1:
            sel -= 1
        else:
           break

    count -= sel
    PrintConsole('бот: ', sel)
    return (checkCount(count), count)

def getuser(sel : int):
    res = 0
    while True:
        if sel == 1:
            res = int(input('1 игрок введите число: '))
        else:
            res = int(input('2 игрок введите число: '))
        if res < 29 and res > 0 :
            return res

def checkCount(count:int):
    if count < 1:
        return False
    return True

def User(count, id):
    count -= getuser(id)
    do = checkCount(count)
    return (do, count)

def menu():
    PrintConsole('1 - играть против игрока')
    PrintConsole('2 - играть против бота')
    selUser = input('введите номер: ')
    if selUser == '1':
        return False
    return True

def PrintConsole(stroka:str):
    print(stroka)