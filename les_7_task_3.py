# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой называется элемент ряда,
# делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

import random


def find_median(array):
    for i in array:
        count_1 = 0
        count_2 = 0
        list_v = array.copy()
        list_v.remove(i)
        for j in list_v:
            if j > i:
                count_1 += 1
            else:
                count_2 += 1
        if count_1 == count_2:
            median = i
            return median

if __name__ == '__main__':
    m = 7
    list_base = [random.randint(0, 100) for i in range(2 * m + 1)]
    random.shuffle(list_base)
    print(list_base)
    print(f'Медиана равна: {find_median(list_base)}')

