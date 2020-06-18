sum_numbers = 0

def input_new_numbers(*args):
    global sum_numbers
    while True:
        input_numbers = input('Write numbers using space. Using Enter will sum up all numbers.\nIf you want to break push "a" key: ')
        if input_numbers == 'a':
            break
        list_numbers = list(input_numbers.split(' '))
        list_numbers = list(map(int, list_numbers))
        sum_numbers = sum_numbers+sum(list_numbers)
        print(sum_numbers)

input_new_numbers()


