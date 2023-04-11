# Определить, какое число в массиве встречается чаще всего.
import random
array_1 = [random.randint(1,20) for i in range(1,40)]
print(array_1)
a = array_1[0]
for i in array_1:
    if array_1.count(i) > array_1.count(a):
        a = i
print(a)