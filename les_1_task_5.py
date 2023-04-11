from string import ascii_lowercase as lwr

# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

a = int(input('Введите номер буквы: '))
print(f'Буква под номером {a}:{lwr[a-1]}')