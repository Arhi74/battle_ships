from exceptions import *


class Dot:
    dot_status_dict = {
        'empty': ' О ',
        'ship': ' ■ ',
        'hit': ' X ',
        'miss': ' T ',
        'contour': ' • '
    }

    _status = 'empty'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if value not in self.dot_status_dict.keys():
            raise DotStatusException
        else:
            self._status = value

    def get_status(self):
        return self._status

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return self.dot_status_dict.get(self.status)


class Ship:

    def __init__(self, size, dot_tuple):
        self.health = size
        self.dot_tuple = dot_tuple

    # Уменьшает хп корабля и возвращает оставшиеся хп
    def hit_ship(self):

        if self.health > 0:
            self.health -= 1
            return self.health
        else:
            raise ShipHealthException


class Board:

    def __init__(self, board_size, hid):
        self.board_size = board_size
        self.hid = hid
        self.dots_list = [Dot(x, y) for y in range(1, board_size + 1) for x in range(1, board_size + 1)]
        self.ships_list = []

    # Метод add_ship, который ставит корабль на доску (если ставить не получается, выбрасываем исключения).
    def add_ship(self, vertically, size, **coordinates):

        dot_list = []
        x, y = coordinates.get('x'), coordinates.get('y')
        bow_dot = self.find_dot(x, y)

        if not bow_dot or bow_dot.get_status() != 'empty':
            raise AddShipOutException

        dot_list.append(bow_dot)
        for shift in range(1, size):
            if vertically:
                dot = self.find_dot(x + shift, y)
            else:
                dot = self.find_dot(x, y + shift)

            if not dot or dot.get_status() != 'empty':
                raise AddShipOutException

            dot_list.append(dot)

        if not self.hid:
            for dot in dot_list:
                dot.status = 'ship'

        new_ship = Ship(size, tuple(dot_list))
        self.ships_list.append(new_ship)
        self.contour(new_ship)

    # Метод contour, который обводит корабль по контуру. Он будет полезен и в ходе самой игры, и в при расстановке
    # кораблей (помечает соседние точки, где корабля по правилам быть не может).
    def contour(self, ship):

        for ship_dot in ship.dot_tuple:
            for shift_x in range(-1, 2):
                for shift_y in range(-1, 2):

                    # Проходим по строкам вокруг точки и наносим контур
                    dot = self.find_dot(ship_dot.x + shift_x, ship_dot.y + shift_y)

                    if not dot or dot in ship.dot_tuple:
                        continue

                    if dot and (dot.get_status() == 'empty' or dot.get_status() == 'miss'):
                        dot.status = 'contour'

    # Удаляем контур после расстановки кораблей
    def del_contour(self):
        for dot in self.dots_list:
            if dot.get_status() == 'contour':
                dot.status = 'empty'

    # Метод, который выводит доску в консоль в зависимости от параметра hid.
    def print_board(self):

        # Печать первой строки координат
        for x in range(self.board_size + 1):

            if x == 0:
                print('   ', end='|')
                continue

            print(f' {x} ', end='|')

        print()

        for x in range(1, self.board_size + 1):

            print(f' {x} ', end='|')

            for y in range(1, self.board_size + 1):
                dot = self.find_dot(x, y)

                # Скрываем корабли противника на доске
                if self.hid and dot.get_status() == 'ship':
                    print(dot.dot_status_dict.get('empty'), end='|')
                else:
                    print(dot, end='|')

            print()

    # Метод для поиска точки на доске по координатам
    def find_dot(self, x, y):

        searched_dot = Dot(x, y)
        for dot in self.dots_list:
            if dot == searched_dot:
                return dot
        else:
            return None

    # Метод, который делает выстрел по доске (если есть попытка выстрелить за пределы и в использованную точку,
    # нужно выбрасывать исключения).
    def shot(self, x, y):

        shot = self.find_dot(x, y)

        if not shot:
            raise ShotOutException

        if (shot.get_status() == 'miss'
                or shot.get_status() == 'contour'
                or shot.get_status() == 'hit'):
            raise WrongShotException

        for ship in self.ships_list:
            for dot in ship.dot_tuple:
                if dot == shot:
                    # Если попали, то переводим статус точки, уменьшаем хп корабля и, если он убит помечаем по контуру
                    shot.status = 'hit'
                    print('Попадание! Еще выстрел!')

                    if not ship.hit_ship():
                        self.contour(ship)
                        self.ships_list.remove(ship)

                    return True

        # Если не ошибка и не попадание, то промах
        shot.status = 'miss'
        return False
