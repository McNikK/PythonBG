num = int(input('Write a number: '))
m = num%10
num = num//10
while num > 0:
    if num%10 > m:
        m = num%10
    num = num//10
print(m)