from typing import Union


def add_field(input_list: list[dict], field_name: str,
              values_to_add: Union[list, callable]) -> list[dict]:
    """
    Добавляет одно поле для списка словарей
    :param input_list: входные данные
    :param field_name: название нового поля
    :param values_to_add: либо список значений для нового поля,
    либо функция для вычисления значения этого поля.
    :return:
    """
    if callable(values_to_add):
        for input_item in input_list:
            input_item[field_name] = values_to_add(input_item)
    else:
        if not (isinstance(values_to_add, list) or
                isinstance(values_to_add, tuple)):
            raise TypeError
        if len(values_to_add) != len(input_list):
            raise ValueError

        for i in range(len(input_list)):
            input_list[i][field_name] = values_to_add[i]
    return input_list
