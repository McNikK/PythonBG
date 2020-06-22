from math import factorial

n = int(input('Write a number: '))

def fact(n):
    fact = [factorial(el) for el in range(1,n+1)]
    yield fact


for el in fact(n):
    print(el)
