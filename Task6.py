# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет 
# с номером. Счастливым билетом называют такой билет 
# с шестизначным номером, где сумма первых трех цифр 
# равна сумме последних трех. Т.е. билет 
# с номером 385916 – счастливый, т.к. 3+8+5 = 9+1+6. 

# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

ticket_num = str(input('Enetr the number on your ticket: '))

if int(ticket_num) > 999999 or int(ticket_num) < 99999:
    print('The number of your ticket must contain six digits. Please try again.')
else:
    first_sum = int(ticket_num[0]) + int(ticket_num[1]) + int(ticket_num[2])
    second_sum = int(ticket_num[-1]) + int(ticket_num[-2]) + int(ticket_num[-3])
    if first_sum == second_sum:
        print('Congratulations! You have a lucky ticket!')
    else:
        print('Sorry, pal. Better luck next time!')



