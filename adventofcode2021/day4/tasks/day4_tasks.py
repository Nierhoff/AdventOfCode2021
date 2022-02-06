import logging # https://docs.python.org/3/howto/logging.html
import sys
import os.path
import numpy as np

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

DIR_PATH: str = os.path.dirname(os.path.realpath(__file__))

class Board(object):
    def __init__(self, board) -> None:
        self.board = board
        self.status = np.zeros((5,5), dtype=int)
        self.numbers = []
        return

    def play(self, number: int) -> None:
        if self.is_done() == False:
            for x in range(5):
                for y in range(5):
                    if self.board[x, y] == number:
                        self.status[x,y] = 1
            self.numbers.append(number)
        return

    def is_done(self):
        x_axis = np.sum(self.status, axis=0)
        for x in range(5):
            if x_axis[x] == 5:
                return True
        y_axis = np.sum(self.status, axis=1)
        for y in range(5):
            if y_axis[y] == 5:
                return True
        return False

    def unmarkedNumbers(self):
        umarked = (self.status - 1) * -1
        return (self.board * umarked)
     
    def winnerRow(self):
        x_axis = np.sum(self.status, axis=0)
        row = np.zeros(5)
        for x in range(5):
            if x_axis[x] == 5:
                row = self.board[:, x].flatten()
        y_axis = np.sum(self.status, axis=1)
        for y in range(5):
            if y_axis[y] == 5:
                row = self.board[y, :].flatten()
        return row

class day4_tasks(object):
    """description of class"""

    def __init__(self, file: str) -> None:
        self.file = None
        self.data = None
        self.lines = None
        self.numbers = []
        self.boards = []
        full_file_path = DIR_PATH + '/'+ file
        if (os.path.exists(full_file_path)):
            self.file = full_file_path
            file = None
            self.load()
        else:
            logging.error('file does not exist: ' + str(full_file_path))
            raise RuntimeError('file does not exist: ' + str(full_file_path))
        return

    def load(self) -> None:
        dtype1 = np.dtype([('action', str), ('power',  np.int64)])
        with open(self.file) as _f:
            self.lines = [line.strip() for line in _f.readlines()]
            # real: 001100010011
            # test: 10111
        self.numbers = [int(line) for line in self.lines[0].split(',')]

        delimiters = [3, 3, 3, 3, 3]
        skiprow = 0
        for line in self.lines:
            if len(line) == 0:
                # new section
                with open(self.file) as _f:
                    board = np.loadtxt(_f, dtype=int, skiprows=skiprow, max_rows=5)
                    self.boards.append(Board(board))
            skiprow += 1
        return

    def play(self, number: int):
        for board in self.boards:
            board.play(number)
        return

    def cehckforwinner(self) -> Board:
        for board in self.boards:
            if board.is_done() == True:
                return board
        return None

    def playAll(self) -> Board:
        for number in self.numbers:
            if self.cehckforwinner() != None:
                return self.cehckforwinner()
            self.play(number)
            if self.cehckforwinner() != None:
                return self.cehckforwinner()
        raise RuntimeError('No winner found')
        return None

    def calc(self) -> int:
        winnerBoard: Board = self.playAll()
        number: int = winnerBoard.numbers[-1]
        unmarkedNumbers = winnerBoard.unmarkedNumbers()
        result: int = number * (unmarkedNumbers.sum())
        logging.info('result: ' + str(result))
        return result

    def calc_last(self) -> int:
        for number in self.numbers:
            self.play(number)
            if sum([board.is_done() for board in self.boards]) == len(self.boards):
                lastBoard = self.boards[0]
                for board in self.boards:
                    if len(lastBoard.numbers) < len(board.numbers):
                        lastBoard = board
        number: int = lastBoard.numbers[-1]
        unmarkedNumbers = lastBoard.unmarkedNumbers()
        result: int = number * (unmarkedNumbers.sum())
        logging.info('result: ' + str(result))
        return result



if __name__ == '__main__':
    file = 'resource/dataset_test.csv'
    run = day4_tasks(file)
    run.calc()
    run.calc_complex()


