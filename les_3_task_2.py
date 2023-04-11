# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# второй массив надо заполнить значениями 0, 3, 4, 5 (помните, что индексация начинается с нуля),
# т. к. именно в этих позициях первого массива стоят четные числа.
import random

array_1 = [random.randint(1,20) for i in range(1,15)]
for elem in array_1:
    if array_1.count(elem) > 1:
        array_1.remove(elem)
array_2 = [array_1.index(i) for i in array_1 if i % 2 == 0]
print(array_1)
print(array_2)