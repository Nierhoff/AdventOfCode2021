import logging # https://docs.python.org/3/howto/logging.html
import sys
import os.path
import numpy as np

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

DIR_PATH: str = os.path.dirname(os.path.realpath(__file__))

class Point():
    def __init__(self, x: int, y: int) -> None:
        self.x: int = int(x)
        self.y: int = int(y)
        return

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __div__(self, number: float):
        return Point(self.x/number, self.y/number)

    def __mul__(self, number: float):
        return Point(self.x*number, self.y*number)

    def sum(self) -> float:
        return (self.x**2 + self.y**2)**0.5

class LineSegment(object):
    def __init__(self, start_point, end_point) -> None:
        self.start_point: Point = start_point
        self.end_point: Point = end_point
        return
    def is_horizontal(self) -> bool:
        if self.start_point.x == self.end_point.x:
            return True
        elif self.start_point.y == self.end_point.y:
            return True
        return False
    def get_points(self):
        self.distance = self.end_point - self.start_point
        unit_steps = max([abs(self.distance.x), abs(self.distance.y)])
        self.unit_slope = self.distance.__div__(unit_steps)
        points = []
        for i in range(int(unit_steps)+1):
            point = self.start_point + self.unit_slope.__mul__(i)
            points.append(point)
        return points

class day5_tasks(object):
    """description of class"""

    def __init__(self, file: str) -> None:
        self.file = None
        self.data = None
        self.lines = []
        self.map = None
        self.map_full = None
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
            lines = [line.strip() for line in _f.readlines()]
            # 9,4 -> 3,4
        for line in lines:
            subelements = line.split(' ')
            start_cor = subelements[0].split(',')
            start_point = Point(start_cor[0], start_cor[1])
            end_cor= subelements[2].split(',')
            end_point = Point(int(end_cor[0]), int(end_cor[1]))
            self.lines.append(LineSegment(start_point, end_point))
        all_points = []
        for line in self.lines:
            all_points.extend(line.get_points())
        max_x = max([point.x for point in all_points])
        max_y = max([point.y for point in all_points])
        self.map = np.zeros((max_x+1, max_y+1))
        self.map_full = np.zeros((max_x+1, max_y+1))
        return

    def get_all_straight_points(self):
        all_points = []
        for line in self.lines:
            if line.is_horizontal():
                all_points.extend(line.get_points())
        return all_points

    def get_all_points(self):
        all_points = []
        for line in self.lines:
            all_points.extend(line.get_points())
        return all_points

    def enrich_simple_map(self):
        for point in self.get_all_straight_points():
            self.map[point.x, point.y] += 1
        return self.map

    def enrich_complex_map(self):
        for point in self.get_all_points():
            self.map_full[point.x, point.y] += 1
        return self.map_full

    def calc(self) -> int:
        self.enrich_simple_map()
        result = (self.map >= 2).sum()
        return result

    def calc_complex(self) -> int:
        self.enrich_complex_map()
        result = (self.map_full >= 2).sum()
        return result

if __name__ == '__main__':
    file = 'resource/dataset_test.csv'
    run = day5_tasks(file)
    run.calc()
    run.calc_complex()


