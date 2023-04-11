# 1. Проанализировать скорость и сложность одного любого алгоритма из разработанных
# в рамках домашнего задания первых трех уроков.
# Оценивается задание №3 из ДЗ №3: # В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
# "les_4_task_1.max_min_1(50)" 1000 loops, best of 5: 34.3 usec per loop - 1 вариант, len = 50
# "les_4_task_1.max_min_1(250)" 1000 loops, best of 5: 170 usec per loop - 1 варинат, len = 250
# "les_4_task_1.max_min_2(50)" 1000 loops, best of 5: 37.2 usec per loop - 2 вариант, len = 50
# "les_4_task_1.max_min_2(250)" 1000 loops, best of 5: 183 usec per loop - 2 вариант, len = 250
# Лучше первый вариант, т.к. тратится меньше времени на выполнение одного обхода списка циклом.

import random
import timeit
import cProfile,profile


def max_min_1(n):
    array = [random.randint(-100,100) for i in range(1,n)]
    max_item = max(array)
    min_item = min(array)
    max_ind = array.index(max_item)
    min_ind = array.index(min_item)
    array[max_ind], array[min_ind] = array[min_ind],array[max_ind]
    return array


def max_min_2(n):
    array = [random.randint(-100,100) for i in range(1,n)]
    max_ind = 0
    min_ind = 0
    for elem in range(len(array)):
        if array[elem] < array[min_ind]:
            min_ind = elem
        elif array[elem] > array[max_ind]:
            max_ind = elem
    array[max_ind],array[min_ind] = array[min_ind],array[max_ind]
    return array

def fun(n:int):
    if n <= 0:
        return 0
    else:
        return fun(n-1) + fun(n-1)

cProfile.run()
