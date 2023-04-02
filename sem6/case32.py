# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
from random import randint
def find_indexes(lst, minimum, maximum):
    return [i for i, x in enumerate(lst) if minimum <= x <= maximum]
list=[randint(1,10) for _ in range(15)]
print(list)
print(find_indexes(list,5,9))