# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

dict_16 = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
dict_16_rev = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
hex_1 = list(input('Введите первое шестнадцатеричное число: ').upper())
hex_2 = list(input('Введите второе шестнадцатеричное число: ').upper())

hex_sum = deque()
hex_mul = deque()

for i in hex_1:
    if i in dict_16.keys():
        hex_1[hex_1.index(i)] = dict_16[i]

for i in hex_2:
    if i in dict_16.keys():
        hex_2[hex_2.index(i)] = dict_16[i]

hex_1 = list(map(int,hex_1))
hex_2 = list(map(int,hex_2))

for i in hex_1:
    if hex_1.index(i) != len(hex_1)-1:
        hex_1[hex_1.index(i)+1] += i*16

for i in hex_2:
    if hex_2.index(i) != len(hex_2)-1:
        hex_2[hex_2.index(i)+1] += i*16

summ_decimal = hex_1[-1] + hex_2[-1]
mul_decimal = hex_1[-1] * hex_2[-1]

while summ_decimal % 16 != 0:
    hex_sum.appendleft(summ_decimal % 16)
    summ_decimal //= 16

while mul_decimal % 16 != 0:
    hex_mul.appendleft(mul_decimal % 16)
    mul_decimal //= 16

hex_sum = list(hex_sum)
hex_mul = list(hex_mul)

for i in hex_sum:
    if i in dict_16_rev.keys():
        hex_sum[hex_sum.index(i)] = dict_16_rev[i]

for i in hex_mul:
    if i in dict_16_rev.keys():
       hex_mul[hex_mul.index(i)] = dict_16_rev[i]


print(f'Сумма чисел равна: {hex_sum}')
print(f'Произведение числе равно: {hex_mul}')
