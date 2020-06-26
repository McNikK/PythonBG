""" создать програмно текстовый файл, записать в него программно набор числе, разделенных пробелами.
Программа должна подсчитовать сумму чисел в файле и выводить ее на экран.
"""

f_object = open('Exr5_text.txt', 'w', encoding='utf-8')
num_inp = input('Write down numbers using space: ')
f_object.writelines(num_inp)
f_object.close()

f_object = open('Exr5_text.txt', 'r', encoding='utf-8')
file = f_object.read()
l_num = list(file.split(' '))
l_num_map = list(map(int, l_num))
sum_number = sum(l_num_map)
print(f'{sum_number} - sum of inputted numbers')
f_object.close()


