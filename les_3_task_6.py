# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random
array_1 = [random.randint(1,15) for i in range(1,15)]
for elem in array_1:
    if array_1.count(elem) > 1:
        array_1.remove(elem)

print(array_1)
max_item = max(array_1)
min_item = min(array_1)
print(min_item)
print(max_item)
array_2 = []
for i in array_1:
    if array_1.index(min_item) > array_1.index(i) > array_1.index(max_item) \
            or array_1.index(min_item) < array_1.index(i) < array_1.index(max_item):
        array_2.append(i)

print(array_2)
print(f'Сумма элементов, находящихся между минимальным и максимальным элементами cписка array_1 равна: {sum(array_2)}')