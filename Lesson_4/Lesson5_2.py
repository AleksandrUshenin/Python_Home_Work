#36. Дан список чисел. Создать список, в который попадают числа, описываемые
#возрастающую последовательность. Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д. Порядок элементов менять нельзя
# [ 1, 2, 3, 4, 6, 7 ]

def ex36(list_num):
    result = []
    for i in range(len(list_num) - 1):
        for u in range(i, len(list_num) - 1):
            if list_num[u] > list_num[i]:
                return [list_num[i], list_num[u]]

    return []

print(ex36([5, 1, 2, 3, 4, 6, 1, 7]))