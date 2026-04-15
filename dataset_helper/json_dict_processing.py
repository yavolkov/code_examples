def extract_nested_value(obj, keys):
    """
    Достает значение по пути ключей.
    """
    cur = obj
    try:
        for key in keys:
            cur = cur[key]
        return cur
    except KeyError:
        return None


def process_dictionary_with_config(dictionary: dict, config: dict) -> dict:
    """
    Достает значения из словаря в соответсвии с конфигом
    """
    processed_values = {}
    for attr, config in config.items():
        if isinstance(config, tuple):
            path, func = config
            proc_val = extract_nested_value(dictionary, path)
            processed_values[attr] = func(proc_val)
        else:
            val = extract_nested_value(dictionary, config)
            processed_values[attr] = val
    return processed_values


def process_list_of_dicts_with_config(list_of_dicts: list[dict],
                                      config: dict) -> list[dict]:
    """
    Достает значения из списка словарей в соответсвии с конфигом
    """
    processed_dicts = []
    for dict_to_process in list_of_dicts:
        processed_dicts.append(
            process_dictionary_with_config(dict_to_process, config)
        )
    return processed_dicts


def create_processor(config: dict, list_processor: bool = False):
    """
    Функция для обработки словаря или
    списка словарей в соотвествии с конфигом
    """
    if list_processor:
        def process(list_of_dicts):
            return process_list_of_dicts_with_config(list_of_dicts, config)
    else:
        def process(dct):
            return process_dictionary_with_config(dct, config)
    return process
