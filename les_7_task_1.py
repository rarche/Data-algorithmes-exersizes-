# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.

import random

list_1 = [i for i in range(-100, 100)]
random.shuffle(list_1)
print(list_1)


def bubble_sort(array):
	ind = len(array)
	while ind != 0:
		for i in range(0, ind-1):
			if array[i] > array[i+1]:
				array[i], array[i+1] = array[i+1], array[i]
		ind -= 1
	return array


bubble_sort(list_1)
print(list_1)
