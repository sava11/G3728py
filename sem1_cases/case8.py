# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
x=int(input("Введите число плиточек по горизонтали: "))
y=int(input("Введите число плиточек по вертикали: "))
k=int(input("Введите сколько хотите отломать: "))
print("отломал" if (k%min(x,y)==0 and k<x*y) else "не отломал")