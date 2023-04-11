# 1. Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за четыре квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple

Factory = namedtuple('Factory','name profit')
factory_list = []
profit_list = []
n = int(input('Введите количество предприятий: '))
for i in range(1,n+1):
    name = input(f'Введите наименование предприятия №{i}: ')
    profit = int(input(f'Введите прибыль за 4 квартала для предприятия №{i}: '))
    fact = Factory(name,profit)
    profit_list.append(fact.profit)
    factory_list.append(fact)
mean = sum(profit_list)/n
print(f'Средняя для всех предприятий прибыль за год составляет: {mean}')
print(f'Наименования предприятий, прибыль которых выше средней: {[i.name for i in factory_list if i.profit > mean]}')