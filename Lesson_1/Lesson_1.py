#from ctypes import pointer
import math
#from unittest import case
#from nis import match


def lesson1():
    x = int(input("add x: "))
    y = int(input("add y: "))

    if x < 0 and y > 0:
        print('1')
    elif x > 0 and y > 0:
        print('2')
    elif x < 0 and y < 0:
        print('3')
    elif x > 0 and y < 0:
        print('4')

def lesson2():
    select = input("add quarter number: ")
    #input(u''.join("âöâöâ"))
        
    if select == "1":
        print("x min = -1, x max = -20", "y min = 1, max = 20")
    elif  select == "2":
        print("x min = 1, x max = 20", "y min = 1, max = 20")
    elif select == 3:
        print("x min = -1, x max = -20", "y min = -1, max = -20")
    else:
        print("x min = 1, x max = 20", "y min = -1, max = -20")

def add_cordinates():
    x = int(input("add x: "))
    y = int(input("add y: "))
    return [x, y]

def lesson3():
    point1 = add_cordinates()
    point2 = add_cordinates()

    print(point1)
    print(point2)

    result = (point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2
    result = math.sqrt(result)
    print(result)

print('start')
#lesson1()
#lesson2()
#lesson3()
