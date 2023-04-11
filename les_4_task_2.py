# Решето Эратосфена (очень извращенное, ни разу не оптимизированное) - 1 вариант
# "les_4_task_2.Eratosfen(10)" 1000 loops, best of 5: 7.21 usec per loop - 10
# "les_4_task_2.Eratosfen(100)" 1000 loops, best of 5: 1.06 msec per loop - 100
# "les_4_task_2.Eratosfen(200)" 1000 loops, best of 5: 6.5 msec per loop - 200
# cProfile 38 ncalls - 10
# cProfile 4922 ncalls - 100
# Линейный поиск - 2 вариант
# "les_4_task_2.Simple(10)"
# 1000 loops, best of 5: 118 nsec per loop - 10
# "les_4_task_2.Simple(100)" 1000 loops, best of 5: 120 nsec per loop - 100
# "les_4_task_2.Simple(200)" 1000 loops, best of 5: 122 nsec per loop - 200
# cProfile 1 ncalls - 10
# cProfile 1 ncalls - 100 - Линейная сложность O(n)


import cProfile


def Eratosfen(n):
    lst = list(range(1,n+1))
    smpl = 1
    while smpl != max(lst):
        smpl += 1
        for i in lst[smpl:]:
            if lst[lst.index(i)] != 0:
                if i % smpl == 0:
                    lst[lst.index(i)] = 0
    return smpl

def Simple(n):
    s = 2
    while n % s != 0:
        s += 1
    return s

