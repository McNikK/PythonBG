f_1 = open("lesson1_file.txt", 'w')

while True:
    x = input('Write a line: \n')
    f_1.write(x)
    if x == '':
        break
