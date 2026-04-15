from issue01 import JSON2Py


class ColorizeMixin:
    """
    Mixin that adds color formatting to the string representation
    """
    def __repr__(self):
        text = super().__repr__()
        END = '\033[0'
        START = '\033[1;'
        MOD = 'm'
        return f'{START}{self.repr_color_code}{MOD}{text}{END}{MOD}'


class BaseAdvert(JSON2Py):
    """
    Base advertisement class, based on JSON2Py but
    requiring title and non-negative price.
    """
    def __init__(self, input_data: dict):
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

    def __repr__(self):
        return f"{self.title} | {self.price} ₽"


class Advert(ColorizeMixin, BaseAdvert):
    """
    Advertisement class with colorized output.
    """
    repr_color_code = 32


if __name__ == '__main__':
    iphone_ad = Advert({'title': 'iPhone X', 'price': 100})
    print(iphone_ad)
