import random

# задание 1 простые множители числа N
def exercise1(num):
    result = []
    e = 2
    while num > 1:
        re = num % e
        if re == 0:
            num = int(num / e)
            result.append(e)
        else:
            e = e + 1
    return result

# задание 2 вывод неповторяющих элементов
def exercise2(list_number):
    result = []
    result.append(list_number[0])
    for num in list_number:
        for resNum in result:
            if num != resNum and resNum == result[-1]:
                result.append(num)
            if num == resNum:
                break
    return  result

# сoхранение для задания 3
def saveData(polynomial):
    with open('file.txt', 'w') as data:
        data.write(polynomial)

# задание 3
def exercise3(k):
    res = ''
    for i in range(k, -1, -1):
        a = random.randint(0, 101)
        if i == 0:
            res += str(a)
            break
        else:
            res += str(a) + '*x'
        if i > 1:
            res += '^{}'.format(i)
        res += ' + '
    res += ' = 0'
    saveData(res)
    return res

print(exercise1(1176))

print(exercise2([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

print(exercise3(2))