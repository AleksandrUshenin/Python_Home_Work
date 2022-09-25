
import math
from math import sqrt
from typing import Final
from sympy import *
from symtable import Symbol
import sympy as sy
import matplotlib.pyplot as plt
import numpy as np
#5 * x**2 + 10 + 10 * x -30

def Fx(a, b, c, d, x):
    return a*x**3+b*x**2+c*x+d

def Fx(x):
    return 18 * x**3 + 5 * x**2 + 10 * x -30 

# нахождение корней 
def Find_Corn(x_inp:int):
    a = 18
    b = 5
    c = 10
    d = -30

    x = Fx(x_inp) 
    print(f'\n{x_inp}\n{x}\n')
    if (x > 0):
        x1 = (-b + math.sqrt(x)) / (2 * a)
        x2 = (-b - math.sqrt(x)) / (2 * a)
        print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
        return (x1, x2)
    elif x == 0:
        x1 = -b / (2 * a)
        print("x = %.2f" % x1)
        return (x1, None)
    else:
        print("Корней нет")
        (None, None)

# нахождение инттервала убфвания и врозрастания 
def Find_F(xL, yL):
    res_Down_x = []
    res_Down_y = []
    res_Up_y = []
    res_Up_x = []
    for i in range(1, len(yL)):
        if (i > i - 1):
            res_Up_y.append(yL[i]) 
            res_Up_x.append(xL[i])
        elif (i < i - 1):
            res_Down_y.append(yL[i]) 
            res_Down_x.append(xL[i])
    print(f'интервал возрастания: \ny{res_Up_y} \nx{res_Up_x} ', f'\nинтервал убывания: \ny{res_Down_y} \nx{res_Down_x}')

# отрисовка графика
def Print_graph(x:list, y:list):
    plt.plot(xx, yy)
    plt.grid() 
    plt.show()

xx = []
yy = []

for i in range(-10, 11):
    Find_Corn(i)
    xx.append(i)
    yy.append(Fx(i))

Find_F(xx, yy)
Print_graph(xx, yy)

