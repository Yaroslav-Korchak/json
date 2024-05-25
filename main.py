"""Вам дан json-файл с новостями. Написать программу, которая будет выводить топ 10 самых часто встречающихся в новостях слов длиннее 6 символов.

Приведение к нижнему регистру не требуется.

В результате корректного выполнения задания будет выведен следующий результат:

1
['туристов', 'компании', 'Wilderness', 'странах', 'туризма', 'которые', 'африканских', 'туристы', 'является', 'природы']"""

import json
from pprint import pprint
from collections import Counter


def read_file():
    with open('newsafr.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data
data = read_file()
long_words = []

items = data['rss']['channel']['items']
texts = ' '.join(item['description'] for item in items if 'description' in item)
words = texts.split()
for word in words:
    if len(word) > 6:
        long_words.append(word)
word_counts = Counter(long_words)

top_10_words = [word for word, _ in word_counts.most_common(10)]
print(top_10_words)