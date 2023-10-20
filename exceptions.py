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


class WrongShotException(Exception):

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'WrongShotException, {0} '.format(self.message)
        else:
            return 'В эту точку мы уже стреляли!'


class ShipHealthException(Exception):

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'ShipHealthException, {0} '.format(self.message)
        else:
            return 'ХП корабля <= 0'


class UserAskError(Exception):

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'UserAskError, {0} '.format(self.message)
        else:
            return 'Не могу найти это место на карте, капитан!'
