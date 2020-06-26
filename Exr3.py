import shutil
import sys
import itertools
import math
from functools import reduce

with open(r'D:\Data Science\Основы Python'
          r'\Тестовые занятия'
          r'\Lesson5\Exr_3.txt', 'r',
          encoding='utf-8') as orig_f:
    content = orig_f.readlines()
    updated_content = []

    for i in content:
        updated_content.append(i.strip())

    for i in range(len(updated_content)):
        updated_content[i] = updated_content[i].split(' ')

    head = []
    for sublist in updated_content:
        head.append(sublist[:1])
    head = reduce(lambda x,y: x+y, head)

    tail = []
    for sublist in updated_content:
        tail.append(sublist[1:])
    tail = reduce(lambda x,y: x+y,tail)
    map_obj = map(float, tail)
    tail = list(map_obj)
    avr_income = sum(tail)/len(tail)
    print(f'Average income : {avr_income:.2f}')

    res_dict  = dict(zip(head,tail))

    new_dict = {k: v for k,v in res_dict.items() if v <=20000}

    for key in new_dict:
        print(key)



