# Задача 10: 
# На столе лежат n монеток. 
# Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное 
# число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной 
# и той же стороной. Выведите минимальное 
# количество монет, которые нужно перевернуть. 
# С клавиатуры вводятся число монет и сами монеты построчно.

# Пример:
# Ввод: 1 1 1 1 0 0 -> 2

count = int(input('Please enter the number of coins: '))
heads_count = 0
tails_count = 0

for i in range(count):
    n = int(input("Enter coin's side (0 for heads and 1 for tails): "))
    if n == 0:
        heads_count += 1
    else:
        tails_count += 1

if heads_count >= tails_count:
    print(f'You have to flip {tails_count} coin(s)')
else:
    print(f'You have to flip {heads_count} coin(s)')