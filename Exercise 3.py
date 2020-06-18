def sum_of_3_numbers(x, y, z):
    n_list = [x, y, z]
    s_list = sorted(n_list)
    r_list = s_list[::-1]
    result = r_list[0]+r_list[1]
    return result

num_1 = int(input('Write number No1: '))

if num_1 < 0:
    print('Number is < 0!')
    num_1 = int(input('Write number 1: '))

num_2 = int(input('Write number No2: '))

if num_2 < 0:
    print('Number is < 0!')
    num_2 = int(input('Write number 1: '))

num_3 = int(input('Write number No3: '))

if num_3 < 0:
    print('Number is < 0!')
    num_3 = int(input('Write number 1: '))

print(sum_of_3_numbers(num_1, num_2, num_3))