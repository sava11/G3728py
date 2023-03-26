# В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растет на круглой грядке, причем кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, 
# поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.
from random import randint
def circ(a,mn,mx):
    return a%mx+mn
N=7
arr=[randint(1,15) for e in range(N)]
maxs_arr=[]
for e in range(len(arr)):
    maxs_arr.append(arr[circ(e-1,0,N)]+arr[e]+arr[circ(e+1,0,N)])
print("максимально больше число собранных ягод с куста: {}".format(maxs_arr[maxs_arr.index(max(maxs_arr))]))
print("индекс конкретного куста: {}".format(maxs_arr.index(max(maxs_arr))))