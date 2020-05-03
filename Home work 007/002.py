# Дан список, заполненный произвольными числами. Получить список из элементов исходного, удовлетворяющих следующим
# условиям:
#
#     Элемент кратен 3,
#     Элемент положительный,
#     Элемент не кратен 4.
#
# Примечание: Список с целыми числами создайте вручную в начале файла. Не забудьте включить туда отрицательные числа.
# 10-20 чисел в списке вполне достаточно.


raw_list = [1, 2, 15, 60, -18, 33, -1, 5, 6, 7, 8, -10]

new_list = [number for number in raw_list if number % 3 == 0 and number > 0 and number % 4]

print(new_list)