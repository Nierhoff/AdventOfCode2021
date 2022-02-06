import logging # https://docs.python.org/3/howto/logging.html
import sys
import os.path
import numpy as np

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

DIR_PATH: str = os.path.dirname(os.path.realpath(__file__))

class day7_tasks(object):
    """description of class"""

    def __init__(self, file: str) -> None:
        self.file = None
        self.initial = []
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
        with open(self.file) as _f:
            self.initial = np.genfromtxt(_f, dtype=int, delimiter=',')
        return
    def calc_all(self):
        all = []
        for x in range(self.initial.max()+1):
            all.append(self.get_fuel(x))
        return all
    def get_position(self) -> int:
        all = self.calc_all()
        low = min(all)
        index = all.index(low)
        return index
    def get_fuel(self, pos: int) -> int:
        return np.absolute(self.initial - pos).sum()
    def calc(self):
        pos = self.get_position()
        fuel = self.get_fuel(pos)
        return fuel

    def calc_progresive_all(self):
        all = []
        for x in range(self.initial.max()+1):
            all.append(self.get_fuel_progresive(x))
        return all
    def get_position_progresive(self) -> int:
        all = self.calc_progresive_all()
        low = min(all)
        index = all.index(low)
        return index
    def get_fuel_progresive(self, pos: int) -> int:
        dist = np.absolute(self.initial - pos)
        cost = [sum(range(d+1)) for d in dist]
        return sum(cost)
    
    def calc_progresive(self):
        pos = self.get_position_progresive()
        fuel = self.get_fuel_progresive(pos)
        return fuel

if __name__ == '__main__':
    file = 'resource/dataset_test.csv'
    run = day7_tasks(file)
    run.calc()
    run.calc_complex()


