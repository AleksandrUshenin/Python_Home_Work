
import HomeWorc5_2 as exe2

import HomeWork5_3 as exe3

def exercise1(text : str):
    list_text = text.split(' ')
    result = []
    for line in list_text:
        if  not('абв' in line):
            result.append(line)
    return result

#print(exercise1('абв щцхыша ох цуалцхз мшохщльм зщвлм хщмлыхлабвсмьы хщшомщ лывхдсмло ывсо отывлабвждот зцщоа ывждсабвмл тывз мсщорабв'))

#exe2.exercise2()

exe3.start()