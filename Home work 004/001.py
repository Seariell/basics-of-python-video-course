# Создайте функцию, принимающую на вход имя, возраст и город проживания человека. Функция должна возвращать строку
# вида «Василий, 21 год(а), проживает в городе Москва»

def bio(name, age, city):
    return f'{name}, {age} год(а), проживает в городе {city}'


name = 'Василий'
age = 21
city = 'Москва'

print(bio(name, age, city))