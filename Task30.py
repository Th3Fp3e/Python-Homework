# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов 
# нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: 
# an = a1 + (n-1) * d.
# Каждое число вводится с новой строки

a = int(input('Enter the base number: '))
n = int(input('Enter the number of elements: '))
b = int(input('Enter the step value: '))

for i in range(n):
    print(a + i * b)