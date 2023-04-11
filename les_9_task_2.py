'''
2. Закодируйте любую строку по алгоритму Хаффмана.
'''
import heapq # модуль очереди с приоритетом
from collections import Counter, namedtuple

class Node(namedtuple("Node", ["left","right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + '0')
        self.right.walk(code,acc + '1')


class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc

def huffman_encode(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq,len(h),Leaf(ch))) #len(h) - уникальный атрибут каждого листа, позволяющий проводить сравнение их с узлами
    heapq.heapify(h) # построение очереди с приоритетом
    count = len(h)
    while len(h)>1:
        freq_1,_сount1, left = heapq.heappop(h) #достаем из очереди элемент(лист) с минимальной частотой
        freq_2,count2, right = heapq.heappop(h) #2-ой минимальный (по частоте) за ним элемент(лист)
        heapq.heappush(h, (freq_1 + freq_2, count, Node(left,right))) # добавляем в очередь узел с двумя потомками, являющимися его потомками
        count += 1

    [(_freq, _count, root)] = h
    code = {}
    root.walk(code,'')
    return code

def main():
    s = input('Введите фразу: ')
    code = huffman_encode(s)
    encoded = "".join(code[ch] for ch in s)
    print(len(code), len(encoded))
    for ch in code:
        print(f"{ch}:{code[ch]}")
    print(encoded)
