
#принимаем на вход строку, возвращаем целое число суммы чисел 
def ex1(number):    # задание 1
    line = str(number)
    res = float(0)
    for i in line:
        if i != '.' and i != ',':
            res += float(i)
    return int(res)

# получаем число, возвращаем набор чисел 
def ex2(number):    # задание 2
    result = int(1)
    res = []
    for i in range(1, number + 1):
        result *= i
        res.append(result)
    return res


# перемешиваем получаемый список
def ex3(numbers):   # задание 3
    res = []
    pro = int(0)
    for i in range(0, len(numbers)):
        result = random.randint(0, len(numbers) - 1)
        pro = numbers[i]
        numbers[i] = numbers[result]
        numbers[result] = pro
    print(numbers)


print(ex1(6782))
print(ex1(0.56))

print(ex2(4))

print(ex3([1, 2, 3, 4, 5]))