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
        self.name = _name if isinstance(_name, str) else None
        self.age = _age if isinstance(_age, int) and 0 <= _age <= 200 else None
        if (isinstance(_rating, int) or isinstance(_rating, float)) and 0 <= _rating <= 100:
            self.rating = float(_rating)
        else:
            self.rating = None

    """
    Сражение между двумя спортсменами. После сражения меняется рейтинг у двух атлетов.
    opponent - оппонент нашего спортсмена. Вообще говоря данные записи эквивалентны:
    arm1.fight(arm2) и arm2.fight(arm1)
    Возвращаемое значение отсутствует
    """

    def fight(self, opponent) -> None:  # opponent: Armwrestler, but cant
        ...

    """
    Тренировка спортсмена. Обязательный параметра - кол-во дней тренировки, тип int
    Ничего не возвращает
    """

    def train(self, numOfDays: int) -> None:
        ...


# Машина, которой я являюсь
class Car:
    """
    _name - марка машины, тип str
    _mileage - пробег машины, тип float, измерение в км
    _curPetrol - бензин
    """

    def __init__(self, _name: str, _mileage: float, _curPetrol: float):
        self.name = _name if isinstance(_name, str) else None
        self.mileage = float(_mileage) if isinstance(_mileage, int) or isinstance(_mileage, float) else None
        self.curPetrol = _curPetrol if isinstance(_curPetrol, int) or isinstance(_curPetrol, float) else None

    """
    Поездка. Принимает дистанцию поездки в километрах
    Нет возвращаемого значения
    """

    def drive(self, kilometers: float) -> None:
        ...

    """
    Заправится. Принимает кол-во бензина
    возвращаемого значения Нет
    """

    def refuel(self, fuelAmount: float) -> None:
        ...


class House:
    """
    owner - владелец, тип str
    area - место, тип str
    """

    def __init__(self, _area: str, _owner: str):
        self.owner = _owner if isinstance(_owner, str) else None
        self.area = _area if isinstance(_area, str) else None

    """
    Получить данные о владельце
    Нет параметров
    Возвращает имя владельца
    """

    def getOwner(self) -> str:
        ...

    """
    Изменить местоположение дома
    Принимает номое местоположение, тип стр 
    Возвращает Ничего

    >>> newHouse = House("NewZeland", "Arthur")
    >>> newHouse.getOwner()
    Arthur

    >>> h = House("Mtishe", "Andrey")
    >>> h.getOwner(12)

    typeError: getOwner has no parameters

    """

    def changeArea(self, newArea: str) -> None:
        ...


if __name__ == "__main__":
    import doctest

    doctest.testmod()