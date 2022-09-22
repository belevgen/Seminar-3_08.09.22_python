# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

my_list = [i for i in range(20)]
print(my_list)

def sum_of_odds (my_list):
    sum_odds = 0
    for i in range(1, len(my_list), 2):
        sum_odds += my_list[i]
    return (sum_odds)

print('Сумма на нечетных позициях: ', sum_of_odds(my_list))
