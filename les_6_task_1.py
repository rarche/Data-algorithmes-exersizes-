# Хар-ка версии: 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] win32
from memory_profiler import profile # удобный модуль для вывода подробного отчета используемой памяти в программе

@profile()
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

@profile()
def Simple(n):
    s = 2
    for i in range(2,n):
        if n % s != 0:
            s += 1
        elif n % s == 0:
            n -= 1
    return n

print(Simple(42))
print(Eratosfen(25))