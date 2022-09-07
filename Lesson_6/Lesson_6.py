
from ast import Lambda


def f(res):
    ind, x = res 
    if ind % 2 == 0:
        return False
    return True

def ex1(numbers):
    result = 0
    result_numbers = list(enumerate(numbers))

    result_numbers = list(filter(f, result_numbers))

    for i in result_numbers:
        ind, num = i
        result += num
            
    return result

def exercise1(num):
    result = []
    e = 2
    while num > 1:
        re = num % e
        if re == 0:
            la = lambda x: x / e
            num = int(la(num)) 
            result.append(e)
        else:
            e = e + 1
    return result

#print(exercise1(10))

#print(ex1([2, 3, 5, 9, 3]))
