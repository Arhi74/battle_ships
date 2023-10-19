from exceptions import *


class Dot:

    dot_status_dict = {
        'empty': 'О',
        'ship': '■',
        'hit': 'X',
        'miss': 'T',
        'contour': '•'
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

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return self.dot_status_dict.get(self.status)


class Ship:
    # Длина.
    # Точка, где размещён нос корабля.
    # Направление корабля(вертикальное / горизонтальное).
    # Количеством жизней(сколько точек корабля ещё не подбито).
    def dots(self):
        # Возвращает список всех точек корабля
        pass


class Board:

    # Двумерный список, в котором хранятся состояния каждой из клеток.
    # Список кораблей доски.
    # Параметр hid типа bool — информация о том, нужно ли скрывать корабли на доске (для вывода доски врага) или нет (для своей доски).
    # Количество живых кораблей на доске.

    def __init__(self, board_size, hid):
        self.board_size = board_size
        self.hid = hid
        self.dots_list = [Dot(x, y) for y in range(1, board_size) for x in range(1, board_size)]

    # Метод add_ship, который ставит корабль на доску (если ставить не получается, выбрасываем исключения).
    def add_ship(self):
        pass

    # Метод contour, который обводит корабль по контуру. Он будет полезен и в ходе самой игры, и в при расстановке
    # кораблей (помечает соседние точки, где корабля по правилам быть не может).
    def contour(self):

        pass

    # Метод, который выводит доску в консоль в зависимости от параметра hid.
    def print_board(self):

        # Печать первой строки координат
        for x in range(1, self.board_size + 1):

            if x == 0:
                print(' ', end='|')
                continue

            print(x, end='|')

        print()

        for x in range(1, self.board_size):
            print(x + 1, end='|')

            for y in range(1, self.board_size):
                print(self.find_dot(x, y), end='|')

            print()

    # Метод для поиска точки на доске по координатам
    def find_dot(self, x, y):

        searched_dot = Dot(x, y)
        for dot in self.dots_list:
            if dot == searched_dot:
                return dot
        else:
            raise BoardOutException


    # Метод out, который для точки (объекта класса Dot) возвращает True, если точка выходит за пределы поля, и False, если не выходит.
    def out(self, dot):

        if dot in self.dots_list:
            return False
        else:
            return True

    # Метод, который делает выстрел по доске (если есть попытка выстрелить за пределы и в использованную точку, нужно выбрасывать исключения).
    def shot(self, x, y):

        shot = self.find_dot(x, y)

        print('Выстрел удачный!')
        shot.status = 'miss'



if __name__ == "__main__":
    new_board = Board(6, False)
    new_board.print_board()
    new_board.shot(1, 1)
    new_board.print_board()
