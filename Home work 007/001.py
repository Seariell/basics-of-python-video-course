# Решить с помощью генераторов списка.
# 1: Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.
#
#     Примечание: Списки фруктов создайте вручную в начале файла.

fruits1 = ['яблоки', 'груши', 'вишня', 'агава', 'клубника', 'манго', 'инжир', 'банан', 'ананас', 'черника', 'голубика']
fruits2 = ['малина', 'черника', 'клубника', 'голубика', 'манго', 'клюква', 'банан', 'вишня', 'инжир']

fruits = [fruit for fruit in fruits1 if fruits2.count(fruit)]
print(fruits)