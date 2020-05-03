# Создайте модуль (модуль - программа на Python, т.е. файл с расширением .py). В нем создайте функцию создающую
# директории от dir_1 до dir_9 в папке из которой запущен данный код. Затем создайте вторую функцию удаляющую эти
# папки. Проверьте работу функций в этом же модуле.

import os, sys


def make_dirs():
    for i in range(1, 10):
        path = os.path.join(os.getcwd(), 'dir_{}'.format(i))
        os.mkdir(path)


def del_dirs():
    for i in range(1, 10):
        path = os.path.join(os.getcwd(), 'dir_{}'.format(i))
        os.rmdir(path)
