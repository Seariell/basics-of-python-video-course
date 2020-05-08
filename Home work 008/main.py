import sys
from module_core import create_file, create_folder, get_list, delete_file, copy_file, safe_info, change_dir


safe_info('Старт')


try:
    command = sys.argv[1]
except IndexError:
    print('Отсутствует название команды')
else:
    if command == 'list':
        get_list()
    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название файла')
        else:
            try:
                if sys.argv[3]:
                    create_file(name, sys.argv[3])
            except IndexError:
                create_file(name)
    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название папки')
        else:
            create_folder(name)
    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название файла или папки')
        else:
            delete_file(name)
    elif command == 'copy':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название копируемого объекта')
        else:
            try:
                new_name = sys.argv[3]
            except IndexError:
                print('Отсутствует новое название')
            else:
                copy_file(name, new_name)
    elif command == 'change_dir':
        try:
            path = sys.argv[2]
        except IndexError:
            print('Отсутствует путь')
        else:
            change_dir(path)
    elif command == 'help':
        print('list - список файлов и папок')
        print('create_file - создание файла')
        print('create_folder = создание папки')
        print('delete - удаление файла или папки')
        print('copy - копирование файла или папки')
        print('change_dir - сменить текущую директорию')
    else:
        print('Для помощи введите: main.py help')

safe_info('Конец')
