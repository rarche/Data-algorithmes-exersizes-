# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массивe
import random

array_1 = [random.randint(-15, 15) for i in range(1, 20)]
for elem in array_1:
    if array_1.count(elem) > 1:
        array_1.remove(elem)

a = -16
for i in array_1:
    if a < i < 0:
        a = i

print(array_1)
print(f'Максимальный отрицательный элемент:{a}. Его позиция в списке: {array_1.index(a)}')