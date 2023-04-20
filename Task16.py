# Задача 16: Требуется вычислить, 
# сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число 
# N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

length = int(input('Enter the array length: '))
arr = []

for i in range(1, length + 1):
    arr.append(i)


x = int(input('Enter the element to be counted: '))
count = 0

for j in arr:
    if arr[j - 1] == x:
        count += 1


print(arr)
print(x)
print(f'-> {count}')