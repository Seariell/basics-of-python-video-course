import os
import shutil
import datetime
#
#
def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Такая папка уже есть')


def get_list(folders_only=False):
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


def delete_file(name, forse=0):
    if os.path.isdir(name):
        try:
            os.rmdir(name)
        except OSError:
            if forse:
                delete_folder_forse(name)
            else:
                warn = input(f'Папка {name} не пуста. Все равно удалить? (Да/нет): ')
                if (warn == 'Да') or (warn == 'Д') or (warn == '') or (warn == 'да') or (warn == 'д'):
                    delete_folder_forse(name)
                else:
                    return
    else:
        try:
            os.remove(name)
        except FileNotFoundError:
            print('Нет такого файла или папки')


def delete_folder_forse(name):
    dir_list = os.listdir(name)
    for item in dir_list:
        delete_file(os.path.join(name, item), 1)
    delete_file(name)


def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Такая папка уже есть')
    else:
        shutil.copy(name, new_name)


def safe_info(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')


def change_dir(path):
    try:
        os.chdir(path)
    except FileNotFoundError:
        print('Нет такого пути')


if __name__ == '__main__':
    create_file('test.dat')
    create_file('test1.dat', 'some text')
    create_folder('new_f1')
    get_list()
    get_list(1)
    delete_file('new_f1')
    delete_file('test.dat')
    copy_file('new_f', 'new_f2')
    copy_file('test1.dat', 'test2.dat')
    safe_info('qwe')