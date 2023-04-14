# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. Сколько журавликов сделал 
# каждый ребенок, если известно, что Петя и Сережа сделали 
# одинаковое количество журавликов, а Катя сделала 
# в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10
#     7 -> "нельзя определить"


cranes_num = int(input('Enter the number of cranes that children made: '))

if cranes_num % 6 != 0:
    print('Impossible to calculate with current info')
else:
    boys_made = cranes_num / 6
    katya_made = boys_made * 4
    print(f'Katya made {int(katya_made)} cranes, while both Petya and Sergey only made {int(boys_made)}')