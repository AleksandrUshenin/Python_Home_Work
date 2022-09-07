
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

print(ex1([2, 3, 5, 9, 3]))
