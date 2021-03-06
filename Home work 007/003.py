# Напишите функцию которая принимает на вход список. Функция создает из этого списка новый список из квадратных
# корней чисел (если число положительное) и самих чисел (если число отрицательное) и возвращает результат (желательно
# применить генератор и тернарный оператор при необходимости). В результате работы функции исходный список не должен
# измениться.
# Например:
#
# old_list = [1, -3, 4]
# result = [1, -3, 2]
#
# Примечание: Список с целыми числами создайте вручную в начале файла. Не забудьте включить туда отрицательные числа.
# 10-20 чисел в списке вполне достаточно.

import math

def new_list(lisst):
    result = [round(math.sqrt(number), 2) if number > 0 else number for number in lisst]
    return result

list1 = [1, -3, 4, 5, -6, 15, 49, -81, 25, 16, 7]
print(new_list(list1))


