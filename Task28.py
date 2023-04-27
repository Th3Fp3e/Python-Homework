# Задача 28:
# Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# return sum(a, b) + 1 - такое использовать нельзя

def RecurSum(a, b):
    if a == 0:
        return b
    else:
        return RecurSum(a - 1, b + 1)


n_1 = int(input('Enter the first number: '))
n_2 = int(input('Enter the second number: '))

print(f'The sum of your numbers {n_1} and {n_2} equals {RecurSum(n_1, n_2)}')