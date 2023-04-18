# Задача 14: 
# Требуется вывести все целые степени двойки 
# (т.е. числа вида 2^k), не превосходящие числа N.

# Пример:
# Ввод: 13 -> 1, 2, 4, 8

value = int(input('Enetr your value: '))

power = 0
while 2 ** power <= value:
    print(2 ** power)
    power += 1