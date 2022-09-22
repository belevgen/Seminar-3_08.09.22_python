# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

n = (int(input('Введите десятчное число: ')))
def fib_both_direct(both_limits):
    if both_limits == 0:
        return [0]
    fib_list = [1, 0]
    for i in range(both_limits):
        fib_list.append(fib_list[len(fib_list) - 2] - fib_list[len(fib_list) - 1])
    fib_list.reverse()
    for i in range(both_limits - 1):
        fib_list.append(fib_list[len(fib_list) - 2] + fib_list[len(fib_list) - 1])
    return fib_list


print(f'Список чисел Фибоначчи -{n} to {n}',fib_both_direct(n))