# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

even = odd = 0
num = input('Введите натуральное число: ')
for i in num:
    if int(i) % 2 == 0:
        even += 1
    else:
        odd += 1

print(f'Число {num} содержит в себе {even} четных и {odd} нечетных чисел')
