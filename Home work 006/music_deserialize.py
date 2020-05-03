# Создать модуль music_deserialize.py. В этом модуле открыть файлы group.json и group.pickle, прочитать из них
# информацию. И получить объект: словарь из предыдущего задания.

import json, pickle

with open('group.json', 'r', encoding='utf-8') as f:
    group = json.load(f)

print(group)
print(type(group))

with open('group.pickle', 'rb') as f:
    group2 = pickle.load(f)

print(group2)
print(type(group2))
