f_file = open(r'D:\Data Science\Основы Python'
          r'\Тестовые занятия'
          r'\Lesson5\Exer_4.txt', 'r', encoding="utf-8")

rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

new_file = []

for i in f_file:
    i = i.split(' ', 1)
    new_file.append(rus[i[0]] + ' ' + i[1])
    print(new_file)

f_file.close()

new_file_open = open('Exr4_updated.txt', 'w')
new_file_open.writelines(new_file)

new_file_open.close()

# new_file = []
#     #content = file_obj.read().split('\n')
#     for i in f_file:
#         i = i.split(' ', 1)
#         new_file.append(rus[i[0]] + '  ' + i[1])
#     print(new_file)
#
# with open('file_4_new.txt', 'w') as file_obj_2:
#     file_obj_2.writelines(new_file)