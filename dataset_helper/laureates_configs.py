from json_dict_processing import create_processor
from prizes_configs import prize_processor


def get_year(year_str: str) -> int:
    return int(year_str.split('-')[0]) if year_str is not None else None


CONFIG_PERSON = {
    'id': (['id'], lambda x: int(x)),
    'name': ['knownName', 'en'],
    'gender': ['gender'],
    'birth_year': (['birth', 'date'], get_year),
    'country_birth': ['birth', 'place', 'country', 'en'],
    'country_now': ['birth', 'place', 'countryNow', 'en'],
    'prizes_relevant': (['nobelPrizes'], lambda data: prize_processor()(data))
}


CONFIG_ORG = {
    'id': (['id'], lambda x: int(x)),
    'name': ['orgName', 'en'],
    'founded_year': (['founded', 'date'], get_year),
    'country_founded': ['founded', 'place', 'country', 'en'],
    'country_now': ['founded', 'place', 'countryNow', 'en'],
    'prizes_relevant': (['nobelPrizes'], lambda data: prize_processor()(data))
}


def person_processor():
    return create_processor(CONFIG_PERSON, list_processor=False)


def org_processor():
    return create_processor(CONFIG_ORG, list_processor=False)
