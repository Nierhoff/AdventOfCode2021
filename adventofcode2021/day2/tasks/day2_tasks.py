import logging # https://docs.python.org/3/howto/logging.html
import sys
import os.path
import numpy as np

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

DIR_PATH: str = os.path.dirname(os.path.realpath(__file__))

class day2_tasks(object):
    """description of class"""
    file = None
    data = None
    lines = None

    def __init__(self, file: str) -> None:
        full_file_path = DIR_PATH + '/'+ file
        if (os.path.exists(full_file_path)):
            self.file = full_file_path
            self.load()
        else:
            logging.error('file does not exist: ' + str(full_file_path))
            raise RuntimeError('file does not exist: ' + str(full_file_path))
        return

    def load(self) -> None:
        with open(self.file) as _f:
            self.lines = _f.readlines()
        self.data = []
        for line in self.lines:
            elements = line.split(" ")
            self.data.append({'action': elements[0], 'power': int(elements[1])}) 
        return

    def calc(self) -> int:
        depth: int = 0
        position: int = 0
        aim: int = 0
        for x in self.data:
            logging.info("iteration: {}".format(x))
            if x['action'] == 'forward':
                position += x['power']
            elif x['action'] == 'down':
                depth += x['power']
            elif x['action'] == 'up':
                depth -= x['power']
            else:
                logging.error("iteration: {}".format(x))
        result: int = depth * position
        logging.info("result: {}".format(result))
        return result

    def calc_complex(self) -> int:
        depth: int = 0
        position: int = 0
        aim: int = 0
        for x in self.data:
            logging.info("iteration: {}".format(x))
            if x['action'] == 'forward':
                depth += aim * x['power']
                position += x['power']
            elif x['action'] == 'down':
                aim += x['power']
            elif x['action'] == 'up':
                aim -= x['power']
            else:
                logging.error("iteration: {}".format(x))
        result: int = depth * position
        logging.info("result: {}".format(result))
        return result

if __name__ == '__main__':
    file = 'resource/dataset_test.csv'
    run = day2_tasks(file)
    run.calc()
    run.calc_complex()


