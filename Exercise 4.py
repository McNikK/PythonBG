n_str = str(input('Write a sentence: '))
lstr = n_str.split()
for i, j in enumerate(lstr, 1):
    print(f'{i} {j:.10s}')

