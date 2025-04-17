# Создайте систему бронирования номеров в отеле,
# где разные типы номеров имеют разную стоимость и дополнительные услуги.
#
# Условия:
# Создайте базовый класс HotelRoom с атрибутами:
#
# room_number (номер комнаты)
#
# base_price (базовая цена за ночь)
#
# метод calculate_price(nights), который возвращает стоимость за указанное количество ночей.
#
# Создайте подклассы:
#
# StandardRoom — цена рассчитывается как base_price * nights.
#
# DeluxeRoom — цена включает дополнительно 20% за комфорт (base_price * 1.2 * nights).
#
# SuiteRoom — цена увеличивается на 50%, но включает бесплатный завтрак.

# Напишите функцию book_room(room, nights), которая принимает объект комнаты и количество ночей, а затем возвращает итоговую стоимость.
#
# ```python
# rooms = [
#     StandardRoom(101, 100),
#     DeluxeRoom(202, 150),
#     SuiteRoom(303, 250),
# ]
#
# for room in rooms:
#     print(book_room(room, 3))
import abc
from abc import ABC


class HotelRoom(ABC):
    def __init__(self, room_number, base_price):
        self.room_number = room_number
        self.base_price = base_price

    @abc.abstractmethod
    def calculate_price(self, nights: int) -> int:
        raise NotImplementedError

# StandardRoom — цена рассчитывается как base_price * nights.
#
# DeluxeRoom — цена включает дополнительно 20% за комфорт (base_price * 1.2 * nights).
#
# SuiteRoom — цена увеличивается на 50%, но включает бесплатный завтрак.


class StandardRoom(HotelRoom):
    def calculate_price(self, nights: int) -> int:
        return self.base_price * nights


class DeluxeRoom(HotelRoom):
    def calculate_price(self, nights: int) -> int:
        return self.base_price * 1.2 * nights


class SuiteRoom(HotelRoom):
    def calculate_price(self, nights: int) -> int:
        return self.base_price * 1.5 * nights


room = DeluxeRoom().calculate_price(1)
