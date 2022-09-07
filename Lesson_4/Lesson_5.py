#35. В файле находится N натуральных чисел, записанных через пробел. Среди чисел не
#хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его

def ex35(N: str):
    list_N = N.split()
    list_N = list(map(int, list_N))

    for i in range(1, len(list_N)):
        if list_N[i] - 1 != list_N[i - 1]:
            return list_N[i - 1] + 1
            
    return -1

def ReadFile():
    result = ''

    myfile = open('DataN.txt', 'r')
    result = myfile.readline()
    myfile.close()
    
    return result

N = '1 2 3 4 5 7 8 9' # 6
#N = '1 2 3 5 6 7 8 9'

print(ex35(ReadFile()))