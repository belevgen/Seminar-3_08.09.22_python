# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

my_list = [i for i in range(20)]
print(my_list)

def multiply_pairs(some_list):
    return [some_list[i] * some_list[-i - 1] for i in range((len(some_list) + 1) // 2)]

print('paired multiplication',multiply_pairs(my_list))