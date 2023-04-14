# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 

num = input('Enter a three-digit number:')
result = 0
if int(num) >= 1000 or int(num) < 99:
    print('Please enter a THREE-DIGITS number! (or learn English!)')
else:
    for digit in str(num):
        result += int(digit)
    print(f"The sum of your number's digits is {result}")
