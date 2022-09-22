# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным
# значением дробной части элементов.
## Пример:
## - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

my_float = [1.1, 1.2, 3.1, 5, 10.01]
print(my_float)

def after_the_dot(float_list):
    return [float_list[i] % 1 for i in range(len(float_list))]

temp_list = after_the_dot(my_float)
print('Diff between min and max non-integer parts', max(temp_list) - min(temp_list))