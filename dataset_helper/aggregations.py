import statistics
from dataset_helpers import apply_agg_func


def agg_mean(input_list: list[dict], key: str) -> float:
    """
    Возвращает среднее значение в ключе key у списка словарей input_list
    """
    return apply_agg_func(input_list, key, statistics.mean)


def agg_median(input_list: list[dict], key: str) -> float:
    """
    Возвращает медиану ключа key у списка словарей input_list
    """
    return apply_agg_func(input_list, key, statistics.median)


def top_n(input_list, key, n, reverse=True):
    """
    Возвращает n словарей с наибольшими значениями
    ключа key
    :param input_list: исходный список словарей
    :param key: ключ по которому ищем наибольший
    :param n: сколько элементов надо вернуть
    :param reverse: True - если нужны наибольшие значения ключа, False иначе
    :return:
    """
    valid_data = [item for item in input_list if item.get(key) is not None]
    sorted_data = sorted(valid_data, key=lambda x: x[key], reverse=reverse)
    return sorted_data[:n]
