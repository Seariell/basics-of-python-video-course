# Создайте модуль. В нем создайте функцию, которая принимает список и возвращает из него случайный элемент. Если
# список пустой функция должна вернуть None. Проверьте работу функций в этом же модуле.
#
#     Примечание: Список для проверки введите вручную. Или возьмите этот: [1, 2, 3, 4]


import random

def random_item(var_list):
    if len(var_list) == 0:
        return None
    else:
        return random.choice(var_list)


if __name__ == '__main__':
    test_list = [1, 2, 3, 4]
    print(random_item(test_list))