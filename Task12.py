# Задача 12: 
# Петя и Катя – брат и сестра. 
# Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

# Пример:
# Ввод: 5 6 -> 2 3

sum = int(input('Please enter the sum of two numbers: '))
product = int(input('Please enter the product of two numbers: '))

for i in range(sum):
    for j in range(product):
        if i + j == sum and i * j == product:
            print(f"Petya's numbers are {i} and {j}")