
# задание 1
#суммa элементов списка стоящих на нечётной позиции
def ex1(numbers):
    result = 0
    for i in range(-1, len(numbers), 2):
        if i != -1:
            result += numbers[i]
    return result

# метод к заданию 2
def carrent_number(number):
    res = number / 2
    if res % 1 != 0:
        return int(res) + 1
    return int(res)

# задание 2
#найти произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
def ex2(list_number):
    result = []
    len_list = carrent_number(len(list_number))
    for i in range(len_list):
        result.append(list_number[i] * list_number[len(list_number) - i - 1])
    return  result

# задание 3
#найти разницу между максимальным и минимальным значением дробной части элементов
def ex3(list_numbers):
    min_num = list_numbers[0]
    max_num = 0
    list_result = []
    for i in list_numbers:
        res = round(i % 1, 10)
        if res != 0:
            list_result.append(res)
    for i in list_result:
        if i < min_num:
            min_num = i
        if i > max_num:
            max_num = i
    return max_num - min_num

# задание 4
#преобразовыввает десятичное число в двоичное
def ex4(number):
    result = []
    while number > 0:
        d = number % 2
        result.append(d)
        number = int(number / 2)
    result.reverse()
    print(result)

print(ex1([2, 3, 5, 9, 3]))
print(ex1([1, 9, 6, 4, 2, 11, 19]))

print(ex2([2, 3, 4, 5, 6]))
print(ex2([2, 3, 5, 6]))

print(ex3([1.1, 1.2, 3.1, 5, 10.01]))

ex4(45)
