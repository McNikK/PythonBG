import random
from random import randint
from random import randrange

r_list = list(el*randrange(1,31,3) for el in range(1, 10))
print(r_list)

result = []

for i in range(len(r_list)-1):
    if r_list[i] < r_list[i+1]:
        result.append(r_list[i+1])
print(result, 'cycle')

n_result = [r_list[el+1] for el in range(len(r_list)-1) if r_list[el] < r_list[el+1]]
print(n_result, 'through generator')

