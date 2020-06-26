file_open = open(r'D:\Data Science\Основы Python'
                 r'\Тестовые занятия\Lesson5'
                 r'\exer_2.txt', 'r')

content = file_open.readlines()

line_numbers = len(content)
print(line_numbers, 'Lines in the file!')

for word in range(len(content)):
    print('{} word(s) in line {}'. format(content[word].count(' '), word+1))

