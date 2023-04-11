# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random
array_1 = [random.randint(1,15) for i in range(1,15)]
for elem in array_1:
    if array_1.count(elem) > 1:
        array_1.remove(elem)
print(array_1)
max_item = max(array_1)
min_item = min(array_1)
print(max_item)
print(min_item)
array_1[array_1.index(max_item)], array_1[array_1.index(min_item)] = array_1[array_1.index(min_item)],array_1[array_1.index(max_item)]
print(array_1)
