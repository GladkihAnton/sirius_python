class Car1Assotition:
    def __init__(self, name, wheels, engine):
        self.wheels = wheels
        self.engine = engine
        self.name = name


class CarComposition:
    def __init__(self, name):
        self.engine = Engine(100)
        self.wheels = [Wheel(), Wheel(), Wheel(), Wheel()]
        self.name = name


class Engine:
    def __init__(self, power: int):
        self.power = power


class Wheel:
    def __init__(self):
        ...


class Backet:
    ...


class Profile:
    def __init__(self):
        self.email = ...
        self.backet = Backet()


if __name__ == '__main__':
    engine = Engine(100)
    wheel1 = Wheel()
    wheel2 = Wheel()
    wheel3 = Wheel()
    wheel4 = Wheel()

    # ассоциация
    car1 = Car1Assotition('первая', [wheel1, wheel2, wheel3, wheel4], engine)
    print(f'Мощность двигателя у машины "{car1.name}" = {car1.engine.power}')


    # композиция
    car2 = CarComposition('вторая')
    print(f'Мощность двигателя у машины "{car2.name}" = {car2.engine.power}')
