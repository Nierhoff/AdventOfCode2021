import logging # https://docs.python.org/3/howto/logging.html
import sys
import os.path
import numpy as np
from numpy.linalg import inv
from numpy.linalg import linalg
from scipy.signal import argrelextrema

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

DIR_PATH: str = os.path.dirname(os.path.realpath(__file__))

def local_minima(array2d):
    return ((array2d <= np.roll(array2d,  1, 0)) &
            (array2d <= np.roll(array2d, -1, 0)) &
            (array2d <= np.roll(array2d,  1, 1)) &
            (array2d <= np.roll(array2d, -1, 1)))

class basin(object):
    def __init__(self, x, y, height_map):
        self.x = x
        self.y = y
        self.height_map = height_map
        return None
    def get_basin_map(self):
        self.basin_area = np.zeros(self.height_map.shape, dtype=int)
        self.basin_area[x, y] = 1


        return None

class day9_tasks(object):
    """description of class"""

    def __init__(self, file: str) -> None:
        self.file = None
        self.line_segments = []
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
            self.height_map = np.genfromtxt(_f, dtype=int, delimiter=1)
        return
    def get_neighbours(self, x: int, y: int):
        shape = self.height_map.shape
        result = []
        if x-1 >= 0:
            left = self.height_map[x-1, y]
            result.append(left)
        else:
            left = 10
        if x+1 < shape[0]:
            right = self.height_map[x+1, y]
            result.append(right)
        else:
            right = 10

        if y-1 >= 0:
            lower = self.height_map[x, y-1]
            result.append(lower)
        else:
            lower = 10
        if y+1 < shape[1]:
            upper = self.height_map[x, y+1]
            result.append(upper)
        else:
            upper = 10
        return result
    def get_low_map(self):
        shape = self.height_map.shape
        self.low_map = np.zeros((shape[0], shape[1]), dtype=int)
        
        for x in range(0, shape[0]):
            for y in range(0, shape[1]):
                center = self.height_map[x, y]
                self.low_map[x ,y] = center < min(self.get_neighbours(x, y))
        return self.low_map
    def get_risk_map(self):
        local_low_map = self.get_low_map()
        risk_map = np.zeros(self.height_map.shape, dtype=int)
        risk_map[local_low_map == 1] = self.height_map[local_low_map == 1] + 1
        return risk_map
    def get_basin_size(self):
        low_map = self.get_low_map()
        return

    def calc(self) -> int:
        count = 0
        for segment in self.line_segments:
            count += count_short(segment.output.parts)
        return count
    def calc_output_value(self) -> int:
        count = 0
        for segment in self.line_segments:
            logging.info("known segments input:{}, output:{}".format(count_short(segment.input.parts), count_short(segment.output.parts)))
        array = segment.solve()
        return array.sum()

if __name__ == '__main__':
    file = 'resource/dataset_test.csv'
    run = day5_tasks(file)
    run.calc()
    run.calc_complex()


