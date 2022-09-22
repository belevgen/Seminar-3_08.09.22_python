# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
## Пример:
## - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = (int(input('Введите десятчное число: ')))
def dec_2_bin(dec_number):
    binary_list = []
    binary = 0
    while dec_number > 0:
        binary_list.append(dec_number % 2)
        dec_number = dec_number // 2
    binary_list.reverse()
    for i in range(len(binary_list)):
        binary = 10 * binary + binary_list[i]
    return binary

print(n, "= в двоичном", dec_2_bin(n))