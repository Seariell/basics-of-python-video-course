# Создайте модуль main.py. Из модулей реализованных в заданиях 1 и 2 сделайте импорт в main.py всех функций. Вызовите
# каждую функцию в main.py и проверьте что все работает как надо.
#
# Примечание: Попробуйте импортировать как весь модуль целиком (например из задачи 1), так и отдельные функции из
# модуля.


import module_001
from module_002 import random_item

# module_001.make_dirs()
# module_001.del_dirs()
list1 = [1, 3, 5, 7]
print(random_item(list1))