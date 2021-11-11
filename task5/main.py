import json


class BaseAdvert:
    def __repr__(self):
        return f'{self.title} | {self.price} ₽'


class ColorizeMixin:
    def __init__(self):
        pass

    def __repr__(self):
        repr_str = super().__repr__()
        colour = self.repr_color_code
        return f"\033[{colour}m" + repr_str + "\033[0m"


class Advert(ColorizeMixin, BaseAdvert):
    repr_color_code = 32  # green

    def __init__(self, mapping, public=True):
        super().__init__()

        self.mapping = mapping
        self.public = public

        if not self.public:
            return

        if "price" in self.mapping:
            if self.mapping["price"] < 0:
                raise ValueError("price must be >= 0")
        else:
            self.mapping["price"] = 0

    def __getattr__(self, item):
        if item[-1] == "_":
            return Advert(self.mapping[item[:-1]], False)
        return Advert(self.mapping[item], False)

    def __setattr__(self, key, value):
        if key == "mapping":
            self.__dict__[key] = value
            return
        if key == "price" and value < 0:
            raise ValueError("price must be >= 0")
        self.__dict__[key] = value

    def __str__(self):
        if self.public:
            return self.__repr__()
        return f'{self.mapping}'


if __name__ == '__main__':
    lesson_str = """{ 
        "title": "python", 
        "price": 0, 
        "location": { 
            "address": "город Москва, Лесная, 7", 
            "metro_stations": ["Белорусская"] 
            } 
        }"""
    lesson = json.loads(lesson_str)
    print(lesson)
    lesson_ad = Advert(lesson)
    # обращаемся к атрибуту location.address
    print(lesson_ad.location.address)
    # Out: 'город Москва, Лесная, 7'

    print(lesson_ad.title)

    print(lesson_ad)

    # print(lesson_ad.asdfdsd)
    # KeyError

    lesson_str = '{"title": "python", "price": -1}'
    lesson = json.loads(lesson_str)
    print(lesson)
    # lesson_ad = Advert(lesson)

    lesson_str = '{"title": "python"}'
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    print(lesson_ad.price)
    lesson_ad.price = 10  # or change to -10
    print(lesson_ad.price)

    corgi = """{ 
  "title": "Вельш-корги", 
  "price": 1000,
  "class": "dogs", 
  "location": { 
    "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25" 
  } 
} """
    corgi_map = json.loads(corgi)
    corgi_ad = Advert(corgi_map)
    print(corgi_ad)
    print(corgi_ad.class_)
