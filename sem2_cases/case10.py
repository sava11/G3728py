# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

from random import randint
mass=[bool(randint(0,1)) for e in range(0,randint(8,10))]
side1=0
side2=0
print(mass)
for e in mass:
    if e == True:
        side1+=1
    else:
        side2+=1
print(min(side1,side2))