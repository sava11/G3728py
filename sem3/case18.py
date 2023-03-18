# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# Считываем размер массива
N = int(input("Введите размер массива: "))

from random import randint
mass=[randint(0,99) for e in range(0,N)]
print(mass)
# Считываем число X
X = int(input("Введите число X: "))

# Находим самый близкий элемент к X
min_diff = abs(mass[0] - X)
closest_element = mass[0]
for i in range(1, N):
    diff = abs(mass[i] - X)
    if diff < min_diff:
        min_diff = diff
        closest_element = mass[i]

# Выводим результат
print("Самый близкий элемент к X:", closest_element)