'''
1. Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
'''


import hashlib

def hash_search(s:str,s_sub:str) -> int:
    assert len(s) > 0 and len(s_sub) > 0, 'Строки не могут быть пустыми'
    assert len(s) > len(s_sub), 'Подстрока должна быть короче строки'

    len_sub = len(s_sub)
    h_subs = hashlib.sha1(s_sub.encode('utf-8')).hexdigest()
    count = 0

    for i in range(len(s) - len_sub + 1):
        if h_subs == hashlib.sha1(s[i:i + len_sub].encode('utf-8')).hexdigest():

            if s[i:i + len_sub] == s_sub:
                count += 1

    if count == 0:
        return 'Подстрока не найдена'

    return f'Количество вхождений подстроки "{s_sub}" в строку "{s}" : {count}'

print(hash_search('I fear no man, but that thing - it scares me','t'))
print(hash_search('I fear no man, but that thing - it scares me','e'))
print(hash_search('I fear no man, but that thing - it scares me','th'))