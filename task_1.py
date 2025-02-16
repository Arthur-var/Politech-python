class Vehicle:
    """
    Класс Vehicle представляет общее транспортное средство.

    Атрибуты:
        model (str): Модель транспортного средства.
        speed (int): Максимальная скорость транспортного средства.

    Исключения:
        TypeError: Если model не является строкой или speed не является числом.
        ValueError: Если speed меньше 0.
    """

    def __init__(self, model: str = 'Lada', speed: int = 60):
        """
        Инициализация объекта Vehicle.

        Параметры:
            model (str): Модель транспортного средства (по умолчанию 'Lada').
            speed (int): Максимальная скорость транспортного средства (по умолчанию 60).

        Исключения:
            TypeError: Если model не является строкой или speed не является числом.
            ValueError: Если speed меньше 0.
        """
        if not isinstance(model, str):
            raise TypeError("Model must be a string.")
        if not isinstance(speed, (int, float)):
            raise TypeError("Speed must be an integer or float.")
        if speed < 0:
            raise ValueError("Speed must be non-negative.")

        self._model = model
        self._speed = speed

    def __str__(self):
        """Возвращает строковое представление объекта Vehicle."""
        return f"{self.__class__.__name__} {self._model}. Скорость {self._speed}"

    def __repr__(self):
        """Возвращает формальное строковое представление объекта Vehicle."""
        return f"{self.__class__.__name__}(model={self._model!r}, speed={self._speed!r})"

    def print_info(self):
        """Выводит информацию о транспортном средстве."""
        print(f'This is {self._model}, which can accelerate to {self._speed}')

    def get_type(self):
        """Возвращает тип транспортного средства."""
        return f'{self.__class__.__name__}'


class Car(Vehicle):
    """
    Класс Car представляет легковой автомобиль, наследующий от Vehicle.

    Атрибуты:
        model (str): Модель легкового автомобиля.
        speed (int): Максимальная скорость легкового автомобиля.
    """

    def __init__(self, model: str = 'Lada', speed: int = 60):
        """
        Инициализация объекта Car.

        Параметры:
            model (str): Модель легкового автомобиля (по умолчанию 'Lada').
            speed (int): Максимальная скорость легкового автомобиля (по умолчанию 60).
        """
        super().__init__(model, speed)

    def get_type(self):
        """
        Возвращает тип легкового автомобиля.

        Переопределение метода get_type из класса Vehicle позволяет
        предоставить более специфичную информацию о типе транспортного средства.
        В данном случае, метод возвращает строку, указывающую, что это легковой
        автомобиль, а также его модель.

        Возвращает:
            str: Тип легкового автомобиля.
        """
        return f'{self.__class__.__name__} made by {self._model} in USA'


class Truck(Vehicle):
    """
    Класс Truck представляет грузовик, наследующий от Vehicle.

    Атрибуты:
        model (str): Модель грузовика.
        speed (int): Максимальная скорость грузовика.
        height (int): Высота грузовика.

    Исключения:
        TypeError: Если height не является числом.
        ValueError: Если height меньше 0.
    """

    def __init__(self, model: str = 'Lada', speed: int = 60, height: int = 3):
        """
        Инициализация объекта Truck.

        Параметры:
            model (str): Модель грузовика (по умолчанию 'Lada').
            speed (int): Максимальная скорость грузовика (по умолчанию 60).
            height (int): Высота грузовика (по умолчанию 3).

        Исключения:
            TypeError: Если height не является числом.
            ValueError: Если height меньше 0.
        """
        super().__init__(model, speed)
        if not isinstance(height, (int, float)):
            raise TypeError("Height must be an integer or float.")
        if height < 0:
            raise ValueError("Height must be non-negative.")
        # Приватный атрибут для инкапсуляции, так как важна высота грузового автомобиля, чтобы он смог везде проехать
        self.__height = height

    def __repr__(self):
        """Возвращает формальное строковое представление объекта Truck."""
        return f"{self.__class__.__name__}(model={self._model!r}, speed={self._speed!r}, height={self.__height!r})"

    def get_type(self):
        """
        Возвращает тип грузовика.

        Переопределение метода get_type из класса Vehicle позволяет
        предоставить более специфичную информацию о типе транспортного средства.
        В данном случае, метод возвращает строку, указывающую, что это грузовик,
        его модель и высоту.

        Возвращает:
            str: Тип грузовика, включая модель и высоту.
        """
        return f'{self.__class__.__name__} made by {self._model} in USA and it is {self.__height} m height'


if __name__ == "__main__":
    # Создание экземпляров классов Car и Truck
    car = Car()
    truck = Truck('Man', 200)

    # Вывод информации о типах транспортных средств
    print(car.get_type())
    print(truck.get_type())
    # Выводит строковое представление легкового автомобиля
    print(car)
    # Выводит официальное строковое представление легкового автомобиля
    print(repr(car))
    # Выводит строковое представление грузового автомобиля
    print(truck)
    # Выводит официальное строковое представление грузового автомобиля
    print(repr(truck))
