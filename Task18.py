# Задача 18: Требуется найти в массиве A[1..N]
# самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число
# N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X .

# Если таких значений больше одного, вывести первый найденный.

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

length = int(input('Enter the array length: '))
arr = []

for i in range(1, length + 1):
    arr.append(i)

num = int(input('Enter the number to search for: '))
found_num = arr[0]

for j in arr:
    if arr[j-1] > found_num and arr[j-1] < num:
        found_num = arr[j-1]

print(arr)
print(num)
print(f'-> {found_num}')