# Задача 8: Требуется определить,
# можно ли от шоколадки размером n × m долек
# отломить k долек, если разрешается сделать один разлом
# по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
# Числа вводятся построчно.

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

length = int(input('Enter the length of the bar: '))
width = int(input('Enetr the width of the bar: '))
pieces_count = int(input('Enter the desired number of pieces: '))

if (length + width - 1) < pieces_count:
    print("You can't get that many pieces.")
elif pieces_count == 1:
    print('You want to take only one piece? Just eat the whole bar!')
else:
    print('Sure, you can break it to that many pieces')