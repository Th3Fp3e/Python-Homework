# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

list_test = [1, 5, 6, -4, 12, -67, 3, 10, 3, 26, -1, 0]

min_num = int(input('Enter the minimum value: '))
max_num = int(input('Enter the maximum value: '))

for i in range(len(list_test)):
    if min_num <= list_test[i] and list_test[i] <= max_num:
        print(f'{i}({list_test[i]})')