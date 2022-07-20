import re
from typing import Iterator, Iterable, Union, List, Set


def filter_(iterable: Iterator, search_str: str) -> Iterable:
    if not isinstance(search_str, str):
        raise TypeError('Неверный тип запроса. Нужна строка')
    return filter(lambda x: search_str in x, iterable)


def sort_(iterable: Iterator, order: str = 'asc') -> List:
    if order not in ('asc', 'desc'):
        raise ValueError('Неправильный аргумент. Должен передаваться asc или desc')
    if order == 'desc':
        return sorted(iterable, reverse=True)
    return sorted(iterable, reverse=False)


def map_(iterable: Iterator, column: Union[str, int]) -> Iterable:
    if not str(column).isdigit():
        raise TypeError('Номер колонки должен быть числом')
    return map(lambda x: x.split(' ')[int(column)] + '\n', iterable)


def limit_(iterable: Iterator, number: Union[str, int]) -> List:
    if not str(number).isdigit():
        raise TypeError('Тип ввода - не число')
    return list(iterable)[:int(number)]


def unique_(iterable: Iterator, *args) -> Set:
    return set(iterable)


def regex_(iterable: Iterator, search_str: str) -> Iterable:
    regex = re.compile(rf'{str(search_str)}')
    return filter(lambda x: regex.search(x), iterable)

