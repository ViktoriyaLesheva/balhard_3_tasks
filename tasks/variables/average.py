"""
Дано 3 числа.

Нужно написать функцию calc_average(a, b, c),
которая возвращает среднее арифметическое аргументов
и округляет его до 5 знаков после запятой.
"""
from typing import Union


def calc_average(a: int, b: int, c: int) -> Union[int, float]:
    """Возвращает среднее арифметическое аргументов, округленное до 5 знаков
    после запятой

    :param a: первое число
    :param b: второе число
    :param c: третье число

    :return: среднее арифметическое, округленное до 5 знаков
    """
    calc_average = (int(a) + int(b) + int(c)) / 3
    return round(calc_average, 5)


if __name__ == '__main__':
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    c = int(input('Введите третье число: '))
    print(f'Среднее арифметическое: {calc_average(a, b, c)}')
