number = 5
float_num = 5.2
add_num = number + float_num
print(add_num)

name = str(input("What is your name: "))
sur_name = str(input("What is your surname: "))
h_str = "Hello"
print(h_str, name, sur_name, '!')

age = int(input('How old are you: '))

if 0 < age <30:
    print('you are so young!')
if 30 <= age <= 50:
    print('Children have a '
          'lesson adults should learn, '
          'to not be ashamed of failing, '
          'but to get up and try again ')
if age > 50:
    print('Nature gives you the face you'
          ' have at twenty; it is up to '
          'you to merit the face you have at fifty.')
if age < 0:
    print('common - be serious')
