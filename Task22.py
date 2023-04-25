# Задача 22:
# Даны два неупорядоченных набора целых чисел 
# (может быть, с повторениями).
# Выдать без повторений в порядке возрастания 
# все те числа, которые встречаются
# в обоих наборах.

# Пользователь вводит 2 числа. 
# n - кол-во элементов первого множества. 
# m - кол-воэлементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

from random import randint

n_set = set(randint(1, 20) for i in range(int(input('Enter the length of the first set: '))))
print(n_set)

m_set = set(randint(1, 20) for i in range(int(input('Enter the length of the second set: '))))
print(m_set)

s_set = sorted(n_set.intersection(m_set))
print(*s_set)