# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
from random import randint
mass1=[ randint(1,10) for e in range(int(input("количество элементов в первом наборе: ")))]
mass2=[ randint(1,10) for e in range(int(input("количество элементов во втором наборе: ")))]
print(mass1)
print(mass2)
exit_mass=set()
mass1.sort()
mass2.sort()
for e in mass1:
    for e1 in mass2:
        if e==e1 :
            exit_mass.add(e)
print(exit_mass)