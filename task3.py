# Есть три кортежа целых чисел необходимо найти элементы,
# которые есть в каждом из кортежей и находятся
# в каждом из кортежей на той же позиции.

my_tuple1 = (1, 2, 3, 8, 4)
my_tuple2 = (1, 9, 3, 1, 7)
my_tuple3 = (1, 4, 3, 6, 0)

elem_everywhere = []

for el1, el2, el3 in zip(my_tuple1, my_tuple2, my_tuple3):
    if el1 == el2 == el3:
        elem_everywhere.append(el1)

print(f'Элементы, которые есть на одинаковых позициях во всех кортежах: {tuple(elem_everywhere)}')