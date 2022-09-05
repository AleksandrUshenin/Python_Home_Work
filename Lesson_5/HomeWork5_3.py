

def getLine(plase):
    line = ''
    for a in range(3):
        for i in range(3):
            if plase[a][i] == 0:
                line += 'строка {} столбец {} '.format(a, i)
    print(line)

def userInput(plase, player):
    getLine(plase)
    while True:
        selectPlase = int(input('выбирите строку : '))
        selectPlase2 = int(input('выбирите столбец : '))
        if plase[selectPlase][selectPlase2] == 0:
            plase[selectPlase][selectPlase2] = player
            break
    Printer(plase)
    return plase

def Printer(plase):
    line = ''
    for a in range(3):
        for i in range(3):
            if plase[a][i] == 0:
                line += ' . '
            elif plase[a][i] == 1:
                line += ' X '
            else:
                line += ' O '
        print(line)
        line = ''

def checkWin(plase, player):
    win1 = []
    win2 = []
    win3 = []
    cicl1 = 0
    cicl2 = 0
    cicl3 = 0
    for a in range(3):
        dio = 0
        for i in range(3):
            if plase[a][i] == player:
                cicl1 += 1
                win1.append(True)
            else:
                #cicl2 += 1
                win1.append(False)

            if plase[i][a] == player:
                cicl2 += 1
                win2.append(True)
            else:
                win2.append(False)

            if plase[dio][dio] == player or plase[2 - dio][dio] == player:
                cicl3 += 1
                #print('res', a, i, '|', plase[a][i], plase[i][a], dio)
                win3.append(True)
            else:
                win3.append(False)
            dio += 1

    print('c1', cicl1)
    print('c2', cicl2)
    print('c3', cicl3)
    #print('win1', win1)
    #if False in win1 and False in win2 and False in win3:
    if cicl1 == 3 or cicl2 == 3 or cicl3 == 9:
        print('win player', player)
        return False
    return True

def start():
    do = True
    player = 1
    #plase = [[True, True, True], [True, True, True], [True, True, True]]
    plase = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    while do:
        userInput(plase, player)
        do = checkWin(plase, player)
        if player == 1:
            player = 2
        else:
            player = 1