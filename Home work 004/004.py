# Давайте усложним предыдущее задание.
# Измените сущности, добавив новый параметр - armor = 1.2 (величина брони персонажа)
# Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно, у вас должно быть 2 функции:
#
#     Наносит урон. Это улучшенная версия функции из задачи 3.
#
#     Вычисляет урон по отношению к броне.
#
# Примечание. Функция номер 2 используется внутри функции номер 1 для вычисления урона и вычитания его из здоровья
# персонажа.

player1 = {'name': input('Введите имя мага: '), 'health': 100, 'damage': 25, 'armor': 1.2}

player2 = {'name': input('Введите имя воина: '), 'health': 120, 'damage': 12, 'armor': 1.5}

def attak(person1, person2):
    person2['health'] -= damage(person1, person2)
    print(f'Игрок {person1["name"]} нанес {damage(person1, person2)} урона игроку {person2["name"]}')
    print(f'Здоровье игрока {person2["name"]} теперь составляет {person2["health"]}')

def damage(person1, person2):
    return person1['damage'] // person2['armor']

attak(player1, player2)
attak(player2, player1)
