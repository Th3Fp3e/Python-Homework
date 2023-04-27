# Задача 26:
# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии


def RaiseToPow(n, m):
    if m == 0:
        return 1
    elif m == 1:
        return n
    else:
        return n * RaiseToPow(n, m - 1)


val = int(input('Enter the base value: '))
pow = int(input('Enter the power to raise to: '))

print(f'Your value {val} in power {pow} equals {RaiseToPow(val, pow)}')
