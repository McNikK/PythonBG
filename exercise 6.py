number_of_goods = int(input('Write number of goods: '))
goods = []
x = 1
for i in range(number_of_goods):
    name_g = str(input(f'Write name of the goods No {i+1}: \n'))
    price = int(input(f'Write price of the goods No {i+1}: \n'))
    qty = int(input(f'Write quantity of the goods No {i+1} unit(s): \n'))
    goods.append((x, {'name': name_g, 'price': price, 'qty': qty}))
    x +=1

f_el,s_el = zip(*goods)
new_dict = {}

n_goods = [i['name'] for i in s_el]
p_goods = [i['price'] for i in s_el]
q_goods = [i['qty'] for i in s_el]
new_dict.update(name = n_goods)
new_dict.update(price = p_goods)
new_dict.update(quantity = q_goods)

for i, j in new_dict.items():
    print(f'{i} : {j}')