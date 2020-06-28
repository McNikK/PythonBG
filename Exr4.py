"""Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости."""

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.police = bool(is_police)

    def go(self):
        print(f'Car has started moving ')

    def stop(self):
        print(f'Car has stopped ')

    def turn(self, direction):
        print(f'The car is moving {direction}')

    def show_speed(self, speed):
        print(f'The car speed is {speed}')


class TownCar(Car):

    name = "GMS"
    auto_model = "Waterfall"
    type = 'Track'

    def show_speed(self, speed):
        if speed > 60:
            print('You are speeding! ')
        else:
            print(f'The car speed is {speed}')

class SportCar(Car):

    name = "Porshe"
    auto_model = "GTS"
    max_speed = 350

class Work(Car):

    name = "Ford"
    auto_model = "F150"
    max_speed = 150


    def show_speed(self, speed):
        if speed > 40:
            print('You are speeding! ')
        else:
            print(f'The car speed is {speed}')


class PoliceCar(Car):

    name = "Porshe"
    auto_model = "GTS"
    max_speed = 350


sport_car = SportCar(200, 'red', 'Nisan', 0)
print(sport_car.name, sport_car.auto_model)
sport_car.go()
sport_car.show_speed(150)
sport_car.turn('left')

t_car = TownCar(70, 'white', 'GMS', 0)
print(t_car.name, t_car.auto_model)
t_car.go()
t_car.turn('right')
t_car.show_speed(90)
