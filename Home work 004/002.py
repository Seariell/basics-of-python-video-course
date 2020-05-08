# Cоздайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.

def max3(a, b, c):
    numbers = [a, b, c]
    max_of_3 = numbers[0]
    for number in numbers:
        if number > max_of_3:
            max_of_3 = number
    return max_of_3

print(max3(13, 135, 65))