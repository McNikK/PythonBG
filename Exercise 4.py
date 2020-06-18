def raising_std(num1, num2):
    result = num1 ** num2
    return result

def raising_none_std(x, y):
    tmp = 1
    for i in range(abs(y)):
        tmp *=x
    result_none_std = 1/tmp
    return result_none_std

number = int(input('Write a number: '))

if number < 0:
    print('the number shall be > 0!')
    number = int(input('Write a number: '))

power_n = int(input('Write a power: '))

if power_n > 0:
    print('the power shall be <0!')
    power_n = int(input('Write a power: '))

print(raising_std(number, power_n), 'standard version')
print(raising_none_std(number, power_n),'none-standard version')
