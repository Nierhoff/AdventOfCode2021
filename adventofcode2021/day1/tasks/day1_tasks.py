import logging # https://docs.python.org/3/howto/logging.html
import sys
import os.path
import numpy as np

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

DIR_PATH: str = os.path.dirname(os.path.realpath(__file__))

class day1_tasks(object):
    """description of class"""

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
            self.data = np.loadtxt(_f, dtype=np.int64)
        return

    def calc(self) -> int:
        increased = 0
        for x in range(1, len(self.data)):
            # logging.info('iteration: ' + str(x))
            if (self.data[x] > self.data[x-1]):
                increased += 1
        logging.info('result: ' + str(increased))
        return increased

    def calc_movingAverage(self) -> int:
        increased = 0
        w: int = 3
        moving_average = np.convolve(self.data, np.ones(w), 'valid') / w
        for x in range(1, len(moving_average)):
            # logging.info('iteration: ' + str(x))
            if (moving_average[x] > moving_average[x-1]):
                increased += 1
        logging.info('result: ' + str(increased))
        return increased



if __name__ == '__main__':
    file = 'resource/dataset.csv'
    run = day1_tasks(file)
    run.calc()
    run.calc_movingAverage()

