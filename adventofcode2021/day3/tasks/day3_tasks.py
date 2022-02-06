import logging # https://docs.python.org/3/howto/logging.html
import sys
import os.path
import numpy as np

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

DIR_PATH: str = os.path.dirname(os.path.realpath(__file__))

class day3_tasks(object):
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
            self.lines = _f.readlines()
            # real: 001100010011
            # test: 10111
        delimiter = np.ones(len(self.lines[0]) - 1, dtype=int)
        if len(delimiter) != (len(self.lines[0]) - 1):
            raise RuntimeError('file format')
        with open(self.file) as _f:
            self.data = np.genfromtxt(_f, dtype=int, delimiter=delimiter)
        if len(self.data[0]) == len('10111') or len(self.data[0]) == len('111000010001'):
            logging.info('fileloaded ok: ' + str(self.file))
        else:
            raise RuntimeError('file format')
        #self.data = []
        #for line in self.lines:
        #    elements = line.split("")
        #    self.data.append({'action': elements[0], 'power': int(elements[1])})
        return

    def decimal_conertor(self, array) -> int:
        local_array = array.flatten()
        array_convertor = np.ones(len(local_array))
        for i in range(len(local_array)):
            array_convertor[i] = 2**i
        array_convertor = np.flip(array_convertor)
        decimal = np.sum(local_array * array_convertor)
        return decimal

    def get_gamma(self) -> int:
        gamma: int = 0
        size: int = len(self.data)
        sums = np.sum(self.data, axis= 0)
        gamma_array = sums > size/2
        gamma = self.decimal_conertor(gamma_array)
        logging.info('gamma: ' + str(gamma))
        return gamma

    def get_epsilon(self) -> int:
        epsilon: int = 0
        size: int = len(self.data)
        sums = np.sum(self.data, axis= 0)
        epsilon_array = sums < size/2
        epsilon = self.decimal_conertor(epsilon_array)
        logging.info('epsilon: ' + str(epsilon))
        return epsilon

    def calc(self) -> int:
        result: int = self.get_gamma() * self.get_epsilon()
        logging.info('result: ' + str(result))
        return result

    def get_co2(self) -> int:
        bits: int = len(self.data[0])
        data_copy = self.data.copy()
        for i in range(bits):
            sums = np.sum(data_copy, axis= 0) < len(data_copy)/2
            filter_arr = []
            for element in data_copy:
                if bool(element[i]) == sums[i]:
                    filter_arr.append(True)
                else:
                    filter_arr.append(False)
            data_copy = data_copy[filter_arr]
            if len(data_copy) == 1:
                break
        result = self.decimal_conertor(data_copy)
        return result

    def get_oxygen(self) -> int:
        bits: int = len(self.data[0])
        data_copy = self.data.copy()
        for i in range(bits):
            sums = np.sum(data_copy, axis= 0) >= len(data_copy)/2
            filter_arr = []
            for element in data_copy:
                if bool(element[i]) == sums[i]:
                    filter_arr.append(True)
                else:
                    filter_arr.append(False)
            data_copy = data_copy[filter_arr]
            if len(data_copy) == 1:
                break
        result = self.decimal_conertor(data_copy)
        return result

    def calc_complex(self) -> int:
        result: int = self.get_co2() * self.get_oxygen()
        logging.info('result: ' + str(result))
        return result



if __name__ == '__main__':
    file = 'resource/dataset_test.csv'
    run = day3_tasks(file)
    run.calc()
    run.calc_complex()


