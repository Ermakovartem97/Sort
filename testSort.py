from random import randint
from time import time


def test_sort(sort_name):

    min_time = 99
    max_time = 0
    min_count = 999999
    max_count = 0

    for i in range(100):
        test_list = [randint(-100, 100) for i in range(400)]  # Создание списков для тестирования

        start_time = time()
        sort = sort_name(test_list)  # Сортировка списков
        work_time = time() - start_time

        min_time = min(work_time, min_time)
        max_time = max(work_time, max_time)
        min_count = min(sort[1], min_count)
        max_count = max(sort[1], max_count)

    solution = [[round(min_time, 2), min_count], [round(max_time, 2), max_count]]  # Результат в формате [время работы, кол-во итераций]

    return (solution)
