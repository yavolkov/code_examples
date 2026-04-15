from collections.abc import Iterable
from collections import defaultdict, Counter


def check_dict_conditions(input_dict: dict, conds: dict) -> bool:
    """
    Проверяет, выполняются ли условия фильтра для словаря
    """
    for key, cond in conds.items():
        value = input_dict.get(key)
        if callable(cond) and not cond(value):
            return False
        elif not callable(cond) and (value != cond):
            return False
    return True


def filter_dicts(input_list: list[dict],
                 conds: dict) -> list[dict]:
    """
    Возвращает из списка словарей те, которые
    удовлетворяют условиям conds
    """
    return [d for d in input_list if check_dict_conditions(d, conds)]


def groupby(input_list: list[dict],
            groupby_columns: Iterable[str]) -> dict:
    """
    Повторяет функционал GROUPBY в SQL
    """
    if isinstance(groupby_columns, str):
        groupby_columns = list(groupby_columns)

    result = defaultdict(list)
    for input_dict in input_list:
        key = tuple([input_dict[k] for k in groupby_columns])
        result[key].append(input_dict)
    return result


def apply_agg_func(input_data: list[dict], key, agg_func):
    """
    Применяет аггрегирующую функцию к конкретному
    ключу
    """
    values = [item[key] for item in input_data if item[key] is not None]
    if values:
        return agg_func(values)
    return None


def select_fields(input_data: list[dict], fields: list[str]) -> list[dict]:
    """
    В каждом словаре списка оставляет только поля fields
    """
    result = []
    for input_item in input_data:
        res_item = dict()
        for key in fields:
            res_item[key] = input_item[key]
        result.append(res_item)
    return result


def select_field(input_data: list[dict], field: str) -> list:
    """
    Возвращает список значений одного поля для
    списка словарей
    """
    res = []
    for input_item in input_data:
        res.append(input_item[field])
    return res


def flatten_prizes(laureates: list[dict]) -> list[dict]:
    """Преобразует вложенные призы в плоский список"""
    flat_prizes = []
    for laureate in laureates:
        for prize in laureate['prizes_relevant']:
            flat_prize = prize.copy()
            flat_prize['laureate_id'] = laureate['id']
            flat_prize['laureate_name'] = laureate['name']
            flat_prize['laureate_type'] = laureate['type_']
            flat_prize['country_now'] = laureate['country_now']
            if laureate.get('type_') == 'person':
                flat_prize['country_birth'] = laureate['country_birth']
                flat_prize['gender'] = laureate['gender']
                flat_prize['birth_year'] = laureate['birth_year']
            else:
                flat_prize['founded_year'] = laureate['founded_year']
                flat_prize['country_founded'] = laureate['country_founded']
            flat_prizes.append(flat_prize)
    return flat_prizes


def top_n_freq(input_list: list[dict], key: str, n: int) -> list[tuple]:
    """
    Возвращает Топ-N самых частых значений в поле
    """
    values = [item[key] for item in input_list if item[key] is not None]
    counter = Counter(values)
    return counter.most_common(n)
