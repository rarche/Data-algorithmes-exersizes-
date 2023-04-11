# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.

import random
array_1 = [random.randint(1,20) for i in range(1,40)]
array_2 = []
print(array_1)
array_2.append(array_1.pop(array_1.index(min(array_1))))
array_2.append(array_1.pop(array_1.index(min(array_1))))
print(f'Два наименьших элемента списка array_1: {array_2}')