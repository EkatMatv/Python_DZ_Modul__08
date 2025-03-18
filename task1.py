# Есть три кортежа целых чисел необходимо найти
# элементы, которые есть во всех кортежах.

my_tuple1 = (1, 2, 3, 8, 4)
my_tuple2 = (4, 9, 3, 1, 7)
my_tuple3 = (2, 4, 1, 6, 0)

all_elements_tuples = []

for num in my_tuple1:
    if num in my_tuple2 and num in my_tuple3:
        all_elements_tuples.append(num)

print(f'Элементы, которые есть во всех кортежах: {tuple(all_elements_tuples)}')