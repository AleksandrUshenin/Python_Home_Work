#class my_class(object):
   # pass
   
def Lesson1():
    number1 = int(input('add number 1: '))
    number2 = int(input('add number 2: '))

    if number1 * number1 == number2 or number2 * number2 == number1:
        print('true')
    else:
        print('false')

def add_number():
    return int(input('add number : '))

def get_numbers():
    numberes = []    
    for i in range(5):     #for (int i = 0; 0 < num; i++)
        numberes.append(add_number())
    return numberes

def get_large_number(numbers):
    number_large = numbers[0]
    for number in numbers:
        if number > number_large:
            number_large = number
    return number_large

def Main():
    print(get_large_number(get_numbers()))

def Main2():
    print_numbers(add_number())

def print_numbers(number):
    for item in range(-number, number + 1):
        print(item)

def get_float():
    return float(input('add number: '))

def Print(str):
    print(str)

def Main3():
    #round(x, n) 
    number  = get_float() * 10
    number = int(number) % 10
    Print(number)

#Lesson1()
#Main()
#Main2()
Main3()