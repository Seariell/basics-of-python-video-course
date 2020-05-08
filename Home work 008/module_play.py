def play():
    number = None
    prompt = None
    min_number = 0
    max_number = 100
    print('Загадайте число от 1 до 100')

    while prompt != '=':
        number = min_number + (max_number - min_number) // 2
        prompt = input(f'Число {number}? ')
        if prompt == '<':
            max_number = number
        elif prompt == '>':
            min_number = number
        elif prompt != '=':
            print('Введите <, есди число меньше')
            print('Введите >, есди число больше')
            print('Введите =, есди число угадано')
    else:
        print(f'Число {number}. Победа!')