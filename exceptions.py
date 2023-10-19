class ShotOutException(Exception):

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'BoardOutException, {0} '.format(self.message)
        else:
            return 'Выстрел за пределы доски! Попробуйте еще раз.'


class DotStatusException(Exception):

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'DotStatusException, {0} '.format(self.message)
        else:
            return 'Неправильно указан статус у точки!'


class ShipBowDotException(Exception):

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'ShipBowDotException, {0} '.format(self.message)
        else:
            return 'Неверно указана начальная точка корабля!'


class AddShipOutException(Exception):

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'AddShipOutException, {0} '.format(self.message)
        else:
            return 'Точка корабля вышла за пределы доски!'
