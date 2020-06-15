n = int(input('Enter number of elements of the list: '))
n_lst = []

if n > 2:
    for i in range(n):
        ele = input('Add element: ')
        n_lst.append(ele)

    x = n_lst[::2]
    y = n_lst[1::2]

    z = [j for i in zip(y, x) for j in i]

    if len(n_lst)%2 == 0:
        print(z)
    else:
        tmp = n_lst[-1]
        z.append(tmp)
        print(z)
else:
    print('Error, number of elements shall be more than 2!')
