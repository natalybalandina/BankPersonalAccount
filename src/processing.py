from typing import List, Dict
from datetime import datetime


def filter_by_state(id_numbers: str, state='EXECUTED': str): -> Dict[str, str]
"""
  Принимает список словарей filter_by_state и значение для ключа state по умолчанию'EXECUTED'.
  Функция возвращает новый список словарей, содержащий только те словари,
  у которых ключ state соответствует указанному значению.

 Функция принимает:
    filter_by_state: Список словарей для фильтрации.
  [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, 
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
  ]
    state: Опциональное значение ключа, по которому фильтруем. По умолчанию 'EXECUTED'.

   Функция возвращает:
    Новый список словарей, удовлетворяющих условию фильтрации.

    Выход функции со статусом по умолчанию 'EXECUTED'
[
  {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

    Выход функции, если вторым аргументов передано 'CANCELED'
[
  {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
] 
"""

filter_default_key = []: -> Dict[str, str]
filter_specified_state = []: -> Dict[str, str]
    for item in id_numbers:
        if item.get('state') == 'state':
            filter_default_key.append(item)
        elif item.get('state') != 'state':
            filter_specified_state.append(item)
        else:
            continue
    return filter_default_key, filter_specified_state

list_of_dictionaries = [
   {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
   {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

executed, canceled = filter_by_state(list_of_dictionaries)
print("Список с указынным значением 'state':", EXECUTED)
print("Список с другим значением 'state':", CANCELED)