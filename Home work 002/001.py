# Даны два произвольные списка. Удалите из первого списка элементы присутствующие во втором списке.
#
#     Примечание. Списки создайте вручную, например так:
#
# my_list_1 = [2, 5, 8, 2, 12, 12, 4]
# my_list_2 = [2, 7, 12, 3]

list1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'q', 'w', 'e', 'r', 't', 'y', 'u']
list2 = ['e', 't', 'u', 'o']

for letter in list2:
    if letter in list1:
        for i in range(list1.count(letter)):
            list1.remove(letter)
print(list1)