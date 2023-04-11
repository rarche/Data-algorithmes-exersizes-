# 1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу).
# Сколько рукопожатий было?

n = int(input('Введите количество встретившихся друзей: '))

g = []
for i in range(n):
    s = [1 for _ in range(n)]
    s[i] = 0
    g.append(s)

handshakes = 0
for items in g:
    for j in items:
        if j == 1:
            handshakes += 1

print(*g,sep='\n')
print(f'Кол-во рукопожатий: {handshakes}')