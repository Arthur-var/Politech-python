# Данный класс представляет собой армрестлера, который присутствует
# в глобальной базе данных армрестлеров
class Armwrestler:
    """
    _name - имя спортсмена. Ожидается тип str
    _age - возраст спортсмена. Ожидается тип int
    _rating - рейтинг в базе данных арма. Ожидается тип float. При получении int
    кастуется до float

    """

    def __init__(self, _name: str, _age: int, _rating: float):
        if isinstance(_name, str):
            self.name = _name
        else:
            raise TypeError('Say my name')

        if not isinstance(_age, int):
            raise TypeError('Say my name')
        if not 0 <= _age <= 200:
            raise ValueError('You god damn right')

        self.age = _age

        if not isinstance(_rating, (int, float)):
            raise TypeError('Say my name')
        if not 0 <= _rating <= 100:
            raise ValueError('You god damn right')

        self.rating = float(_rating)

    def fight(self, opponent) -> None:  # opponent: Armwrestler - так нельзя. А как надо?
        """
        Сражение между двумя спортсменами. После сражения меняется рейтинг у двух атлетов.
        opponent - оппонент нашего спортсмена. Вообще говоря данные записи эквивалентны:
        arm1.fight(arm2) и arm2.fight(arm1)
        Возвращаемое значение отсутствует
        """
        if not isinstance(opponent, Armwrestler):
            raise TypeError('Я хочу пиццу')
        ...

    def train(self, num0fdays: int) -> None:
        """
        Тренировка спортсмена. Обязательный параметра - кол-во дней тренировки, тип int
        Ничего не возвращает
        """
        if not isinstance(num0fdays, int):
            raise TypeError('Саня, покажи спину')
        ...


# Машина, которой я являюсь
class Car:
    """
    _name - марка машины, тип str
    _mileage - пробег машины, тип float, измерение в км
    _curPetrol - бензин
    """

    def __init__(self, _name: str, _mileage: float, _cur_petrol: float):
        if isinstance(_name, str):
            self.name = _name
        else:
            raise TypeError('Say my name')

        if isinstance(_mileage, (int, float)):
            self.mileage = float(_mileage)
        else:
            raise TypeError('Say my name')

        if isinstance(_cur_petrol, (int, float)):
            self.cur_petrol = float(_cur_petrol)
        else:
            raise TypeError('Say my name')

    def drive(self, kilometers: float) -> None:
        """
        Поездка. Принимает дистанцию поездки в километрах
        Нет возвращаемого значения
        """
        if not isinstance(kilometers, (float, int)):
            raise TypeError('я ухожу работать в айти, там платят денег дофига, наконец богатым стану я')
        ...

    def refuel(self, fuel_amount: float) -> None:
        """
        Заправится. Принимает кол-во бензина
        возвращаемого значения Нет
        """
        if not isinstance(fuel_amount, (float, int)):
            raise TypeError('Адский разгон')
        ...


class House:
    """
    owner - владелец, тип str
    area - место, тип str
    """

    def __init__(self, _area: str, _owner: str):
        if isinstance(_owner, str):
            self.owner = _owner
        else:
            raise TypeError('Say my name')

        if isinstance(_area, str):
            self.area = _area
        else:
            raise TypeError('Say my name')

    def get_owner(self) -> str:
        """
        Получить данные о владельце
        Нет параметров
        Возвращает имя владельца

        >>> newHouse = House("NewZeland", "Arthur")
        >>> newHouse.get_owner()
        'Arthur'

        >>> h = House("Mtishe", "Andrey")
        >>> h.get_owner(12)

        typeError: getOwner has no parameters
        """
        ...

    def change_area(self, new_area: str) -> None:
        """
        Изменить местоположение дома
        Принимает номое местоположение, тип стр
        Возвращает Ничего
        """
        if not isinstance(new_area, str):
            raise TypeError('Выигрыш 22 рубля')
        ...


if __name__ == "__main__":
    import doctest

    doctest.testmod()
