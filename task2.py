# Есть три кортежа целых чисел необходимо найти
# элементы, которые уникальны для каждого списка.

my_tuple1 = (1, 2, 3, 8, 4)
my_tuple2 = (4, 9, 3, 1, 7)
my_tuple3 = (2, 4, 1, 6, 0)

uniq_el_tuple1 = [num for num in my_tuple1 if num not in my_tuple2 and num not in my_tuple3]
uniq_el_tuple2 = [num for num in my_tuple2 if num not in my_tuple1 and num not in my_tuple3]
uniq_el_tuple3 = [num for num in my_tuple3 if num not in my_tuple1 and num not in my_tuple2]

print(f'Уникальные элементы для 1-го кортежа {my_tuple1}:  {tuple(uniq_el_tuple1)}\n'
      f'Уникальные элементы для 2-го кортежа {my_tuple2}:  {tuple(uniq_el_tuple2)}\n'
      f'Уникальные элементы для 3-го кортежа {my_tuple3}:  {tuple(uniq_el_tuple3)}\n')