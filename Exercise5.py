from functools import reduce

new_list = [el for el in range(100,1001) if el%2 == 0]
def my_fun(*args):
    result = 1
    for i in new_list:
        result = result * i
    return result

print(reduce(my_fun,new_list))




