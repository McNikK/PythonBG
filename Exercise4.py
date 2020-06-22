import random
from random import randint
from random import randrange

source_list = [el*randrange(1,3) for el in range(100)]
print(source_list)
result = list(dict.fromkeys(source_list))
print(result)

