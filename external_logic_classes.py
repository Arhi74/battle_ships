import random
import os
import time
from internal_logic_classes import Board
from exceptions import *


class Player:

    def __init__(self, board: Board, enemy_board: Board):
        self.board = board
        self.enemy_board = enemy_board

    # Метод, который «спрашивает» игрока, в какую клетку он делает выстрел.
    def ask(self):
        return None, None

    # Метод, который делает ход в игре. Тут мы вызываем метод ask, делаем выстрел по вражеской доске
    # (метод Board.shot), отлавливаем исключения, и если они есть, пытаемся повторить ход.
    # Метод должен возвращать True, если этому игроку нужен повторный ход (например, если он выстрелом подбил корабль).
    def move(self):
        x, y = self.ask()
        try:
            hit = self.enemy_board.shot(x, y)
        except Exception as error:
            print(error)
            return True
        else:
            return hit


class AI(Player):

    def __init__(self, board: Board, enemy_board: Board):
        self.board = board
        self.enemy_board = enemy_board

    def ask(self):
        shot_dot_list = [dot for dot in self.enemy_board.dots_list if dot.get_status() == 'empty'
                         or dot.get_status() == 'ship']
        rand_dot = random.choice(shot_dot_list)
        return rand_dot.x, rand_dot.y

    def __str__(self):
        return 'Компьютер'


class User(Player):

    def ask(self):
        coordinates_list = input('Куда стреляем, капитан? ').split()

        if len(coordinates_list) != 2 or not coordinates_list[0].isdigit() or not coordinates_list[1].isdigit():
            raise UserAskError

        return int(coordinates_list[0]), int(coordinates_list[1])

    def __str__(self):
        return 'Игрок'


class Game:

    def __init__(self, board_size):

        # Для расстановки кораблей заведем список размеров кораблей
        self.ships_list = [3, 2, 2, 1, 1, 1, 1]

        # Заполняем доски
        self.player_board = self.random_board(board_size, False)
        self.computer_board = self.random_board(board_size, True)
        self.player_board.del_contour()
        self.computer_board.del_contour()
        # Создаем игроков
        self.player = User(self.player_board, self.computer_board)
        self.computer = AI(self.computer_board, self.player_board)

    # Метод генерирует случайную доску
    def random_board(self, board_size, hid):

        while True:

            board = Board(board_size, hid)
            # Количество попыток заполнить доску случайно

            for ship_size in self.ships_list:

                for _ in range(1000):

                    coordinates = {
                        'x': random.randint(1, board_size),
                        'y': random.randint(1, board_size)
                    }
                    vertically = random.choice((True, False))
                    try:
                        board.add_ship(vertically, ship_size, **coordinates)
                    except:
                        continue
                    else:
                        break
                # Очистить доску и начать заново
                else:
                    break
            # Удалось расставить корабли
            else:
                return board

    # Метод, который в консоли приветствует пользователя и рассказывает о формате ввода
    @staticmethod
    def greet():
        print('Приветствую, капитан! Добро пожаловать в игру "Морской бой"!\nУспей затопить все корабли компьютера, '
              'прежде, чем он затопит твои!\nКорабли расставлены случайным образом.')
        print('Игра начинается, удачи!')

    # Метод с самим игровым циклом. Там мы просто последовательно вызываем метод mode для игроков и делаем
    # проверку, сколько живых кораблей осталось на досках, чтобы определить победу
    def loop(self):

        current_player, next_player = self.player, self.computer
        while True:

            # Очистка консоли
            time.sleep(5)
            os.system('cls')
            print()

            # Проверка на победу
            if not len(current_player.enemy_board.ships_list):
                print(f'{current_player} победил!')
                break

            # Вывод доски и запрос координат
            next_player.board.print_board()
            print(f'{current_player} ходит:')
            try:
                if current_player.move():
                    pass
                else:
                    print('Промах! Перехожу к следующему игроку')
                    current_player, next_player = next_player, current_player
            except Exception as error:
                print(error)
                continue

    def start(self):
        self.greet()
        self.loop()
