import logging # https://docs.python.org/3/howto/logging.html
import sys
import os.path
import numpy as np

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

DIR_PATH: str = os.path.dirname(os.path.realpath(__file__))

class cave(object):
    def __init__(self, name):
        return None
    def is_big_cave(self):
        return False
    def is_small_cave(self):
        return False

class segment(object):
    def __init__(self, cave1, cave2):
        return None

class routes(object):
    def __init__(self, start):
        self.caves = []
        self.caves.append(start)
        return None
    def is_legal(self):
        for c in self.caves:
            if c.is_small_cave():
                if self.caves.count(c) >= 1:
                    return False

        return False

class day12_tasks(object):
    """description of class"""

    def __init__(self, file: str) -> None:
        self.file = None
        self.line_segments = []
        full_file_path = DIR_PATH + '/'+ file
        self.segments = []
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
            self.lines = [line.strip() for line in _f.readlines()]
        
        for line in self.lines:
            caves = line.split('-')
            self.segments.append(segment(caves[0], caves[1]))
        return
    def calc2(self):
        return 0
    def calc(self) -> int:
        return 0

if __name__ == '__main__':
    file = 'resource/dataset_test.csv'
    run = day10_tasks(file)
    run.calc_syntax_error_score()
    run.calc_autocomplete_score()


