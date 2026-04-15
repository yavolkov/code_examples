from keyword import iskeyword


class JSON2Py:
    """
    Class for converting json object to the python object
    with attribute-style access.
    """
    def __init__(self, input_data: dict):
        for key, value in input_data.items():
            if iskeyword(key):
                key = key + '_'

            if isinstance(value, dict):  # обработка вложенности
                value = JSON2Py(value)
            setattr(self, key, value)


class Advert(JSON2Py):
    """
    Advertisement class, based on JSON2Py but
    requiring title and non-negative price.
    """
    def __init__(self, input_data):
        super().__init__(input_data)

        if not hasattr(self, 'title'):
            raise ValueError("Title отсутствует")

        if not hasattr(self, 'price'):
            self.price = 0

        self.price = self.price  # вызываем setter с проверкой на price>0

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, val):
        if val < 0:
            raise ValueError
        else:
            self._price = val


if __name__ == '__main__':
    iph = {
        "title": "iPhone X",
        "class": "smartphones",
        "location": {
            "address": "город	Самара,	улица	Мориса	Тореза,	50",
            "metro_stations": ["Спортивная", "Гагаринская"]
        }
    }
    neg_price_ex = {
        "title": "Нефть",
        "price": -1000,
    }

    corgi = {
        "title": "Вельш-корги",
        "price": 1000,
        "class": "dogs"
    }

    ad_iph = Advert(iph)
    assert ad_iph.title == "iPhone X"
    assert ad_iph.location.address == "город	Самара,	улица	Мориса	Тореза,	50"
    assert ad_iph.price == 0

    try:
        ad_neg = Advert(neg_price_ex)
    except ValueError:
        print('Защита от отрицательной цены сработала')

    corg_ad = Advert(corgi)
    assert corg_ad.class_ == "dogs"
