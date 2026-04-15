import requests
from typing import Union
from laureates_configs import org_processor, person_processor
URL_LAUREATES = r'https://api.nobelprize.org/2.1/laureates?limit=1200'


def get_laureate_data(laureate: dict) -> Union[dict, None]:
    """
    Извлекает значения из словаря в
    соотвествии с типом лауреата
    """
    if 'knownName' in laureate:
        processed_data = person_processor()(laureate)
        processed_data['type_'] = 'person'
        return processed_data
    elif 'orgName' in laureate:
        processed_data = org_processor()(laureate)
        processed_data['type_'] = 'org'
        return processed_data
    return None


def get_list_of_laureate_data(url: str = URL_LAUREATES) -> list[dict]:
    """
    Обрабатывает список словарей с данными лауреатов
    """
    laureates_data = []
    laureates_response = requests.get(url)
    laureates = laureates_response.json()
    for laureate in laureates['laureates']:
        laureates_data.append(get_laureate_data(laureate))
    return laureates_data
