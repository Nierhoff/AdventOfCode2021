import logging # https://docs.python.org/3/howto/logging.html
import sys
import os.path
import numpy as np
from numpy.linalg import inv
from numpy.linalg import linalg

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

DIR_PATH: str = os.path.dirname(os.path.realpath(__file__))

LETTERS = {
    'a': np.array([1, 0, 0, 0, 0, 0, 0]),
    'b': np.array([0, 1, 0, 0, 0, 0, 0]),
    'c': np.array([0, 0, 1, 0, 0, 0, 0]),
    'd': np.array([0, 0, 0, 1, 0, 0, 0]),
    'e': np.array([0, 0, 0, 0, 1, 0, 0]),
    'f': np.array([0, 0, 0, 0, 0, 1, 0]),
    'g': np.array([0, 0, 0, 0, 0, 0, 1])
    }

DIGITS = {
    #-1: '',                                            #  a  b  c  d  e  f  g
    0: {'txt': 'abcefg',    'len':6,    'array': np.array([1, 1, 1, 0, 1, 1, 1])}, # 7 - d
    1: {'txt': 'cf',        'len':2,    'array': np.array([0, 0, 1, 0, 0, 1, 0])}, # 
    2: {'txt': 'acdeg',     'len':5,    'array': np.array([1, 0, 1, 1, 1, 0, 1])}, # 7 - bf
    3: {'txt': 'acdfg',     'len':5,    'array': np.array([1, 0, 1, 1, 0, 1, 1])}, # 7 - be
    4: {'txt': 'bcdf',      'len':4,    'array': np.array([0, 1, 1, 1, 0, 1, 0])}, #
    5: {'txt': 'abdfg',     'len':5,    'array': np.array([1, 1, 0, 1, 0, 1, 1])}, # 7 - ce
    6: {'txt': 'abdefg',    'len':6,    'array': np.array([1, 1, 0, 1, 1, 1, 1])}, # 7 - c
    7: {'txt': 'acf',       'len':3,    'array': np.array([1, 0, 1, 0, 0, 1, 0])}, #
    8: {'txt': 'abcdefg',   'len':7,    'array': np.array([1, 1, 1, 1, 1, 1, 1])}, #
    9: {'txt': 'abcdfg',    'len':6,    'array': np.array([1, 1, 1, 1, 0, 1, 1])}  # 7 - e
    # a  = len(3):acf - len(2):cf
    # bf = len(4) - len(2)
    # aeg = len(7)abcdefg  - len(4)bcdf
    # ecd = 3*len7:abcdefg - (sum of tree 6)abcdfg:abdefg:abcefg
    # cebebf = 3*len7:abcdefg - (sum of tree 5)abdfg:acdfg:acdegs
    }
def verify():
    for key in DIGITS.keys():
        if (calc_array(DIGITS[key]['txt']) == DIGITS[key]['array']).all() != True:
            raise RuntimeError('wrong array')
        if (len(DIGITS[key]['txt']) == DIGITS[key]['len']) != True:
            raise RuntimeError('wrong length')
    return


DIGITS2 = {
    'abcefg': np.array([1, 1, 1, 0, 1, 1, 1]),
    'cf': np.array([0, 0, 1, 0, 0, 1, 0]),
    'acdeg': np.array([1, 0, 1, 1, 1, 0, 1]),
    'acdfg': np.array([1, 0, 1, 1, 0, 1, 1]),
    'bcdf': np.array([0, 1, 1, 1, 0, 1, 0]),
    'abdfg': np.array([1, 1, 0, 1, 0, 1, 1]),
    'abdefg': np.array([1, 1, 0, 1, 1, 1, 1]),
    'acf': np.array([1, 0, 1, 0, 0, 1, 0]),
    'abcdefg': np.array([1, 1, 1, 1, 1, 1, 1]),
    'abcdfg': np.array([1, 1, 1, 1, 0, 1, 1])
    }

def get_by_letters(letters: str):
    result = []
    for key in DIGITS.keys():
        if DIGITS[key]['txt'] == letters:
            result.append(DIGITS[key])
    if len(result) != 1:
        raise RuntimeError('wrong result set')
    return result[0]

def get_by_length(length: int) -> list:
    result = []
    for key in DIGITS.keys():
        if DIGITS[key]['len'] == length:
            result.append(DIGITS[key])
    return result

def get_by_array(array):
    result = {}
    for key in DIGITS.keys():
        if (DIGITS[key]['array'] == array).all():
            result = DIGITS[key]
    if len(result) != 1:
        raise RuntimeError('wrong result set')
    return result[0]

def calc_array(letters: str):
    part_array = np.zeros(7, dtype=int)
    for letter in sorted(letters):
        part_array += LETTERS[letter]
    return part_array

def get_short(parts) -> int:
    result = []
    for part in parts:
        if len(part) in [len(DIGITS[1]['txt']), len(DIGITS[4]['txt']), len(DIGITS[7]['txt']), len(DIGITS[8]['txt'])]:
            result.append(part)
    return result

def count_short(parts) -> int:
    return len(get_short(parts))

def get_array_with_length(l: int):
    for k in DIGITS.keys():
        if len(DIGITS[k]['txt']) == l:
            return DIGITS[k]['array']
    return None

def loops():
    for k1 in DIGITS.keys():
        for k2 in DIGITS.keys():
            if abs(DIGITS[k1]['array'] - DIGITS[k2]['array']).sum() == 1:
                logging.info("{}:{} - {}:{} = 1".format(k1,DIGITS[k1]['txt'],k2, DIGITS[k2]['txt']))
    logging.info("removing a")
    a_array  = LETTERS['a']
    for k1 in DIGITS.keys():
        k1_array = DIGITS[k1]['array']
        
        for k2 in DIGITS.keys():
            k2_array = DIGITS[k2]['array']
            if k1_array[0] != k2_array[0]:
                if k2_array[0] == 1:
                    k2_array -= a_array
                if k1_array[0] == 1:
                    k1_array -= a_array
                if abs(k1_array - k2_array).sum() == 1:
                    logging.info("{}:{} - {}:{} = 1".format(k1,DIGITS[k1]['txt'],k2, DIGITS[k2]['txt']))

class InputSegment():
    def __init__(self, intput_parts):
        self.parts = intput_parts
        return
    def map(self):
        self.parts_enc = []
        for part in self.parts:
            self.parts_enc.append(calc_array(part))
        return

class OutputSegment():
    def __init__(self, output_parts):
        self.parts = output_parts
        self.map()
        return
    def map(self):
        self.parts_enc = []
        for part in self.parts:
            self.parts_enc.append(calc_array(part))
        return

def find_a(unique_segments):
    # find len=2 and len=3
    for s in [1,4,7,8]:
        if not len(DIGITS[s]['txt']) in [len(u) for u in unique_segments]:
            raise RuntimeError('missing value')
    for u in unique_segments:
        if len(u) == 2:
            el2_array = calc_array(u)
        if len(u) == 3:
            el3_array = calc_array(u)
    a_array = el3_array - el2_array
    if a_array.sum() != 1:
        raise RuntimeError('missing value')
    return a_array

def find_bf(unique_segments):
    # bf = len(4) - len(2)
    for s in [1,4,7,8]:
        if not len(DIGITS[s]['txt']) in [len(u) for u in unique_segments]:
            raise RuntimeError('missing value')
    for u in unique_segments:
        if len(u) == 4:
            el4_array = calc_array(u)
        if len(u) == 2:
            el2_array = calc_array(u)
    bf_array = el4_array - el2_array
    if bf_array.sum() != 2:
        raise RuntimeError('missing value')
    return bf_array

def find_a(unique_segments):
    # find len=2 and len=3
    for s in [1,4,7,8]:
        if not len(DIGITS[s]['txt']) in [len(u) for u in unique_segments]:
            raise RuntimeError('missing value')
    for u in unique_segments:
        if len(u) == 2:
            el2_array = calc_array(u)
        if len(u) == 3:
            el3_array = calc_array(u)
    a_array = el3_array - el2_array
    if a_array.sum() != 1:
        raise RuntimeError('missing value')
    return a_array

def find_d(all_segments):
    # find len=2 and len=3
    for s in [1,4,7,8]:
        if not len(DIGITS[s]['txt']) in [len(u) for u in all_segments]:
            raise RuntimeError('missing value')
    for u in all_segments:
        if len(u) == len('abcdefg'): # 7
            el7_array = calc_array(u)
    d_array = np.zeros(7)
    for u in all_segments:
        if len(u) == len('abcefg'): #6
            el6_array = calc_array(u)
            if abs(el7_array - el6_array).sum() == 1:
                d_array = el7_array - el6_array

    if d_array.sum() != 1:
        raise RuntimeError('missing value')
    return d_array

def find_aeg(unique_segments):
    # aeg = len(7)abcdefg  - len(4)bcdf
    for s in [1,4,7,8]:
        if not len(DIGITS[s]['txt']) in [len(u) for u in unique_segments]:
            raise RuntimeError('missing value')
    for u in unique_segments:
        if len(u) == 7:
            el7_array = calc_array(u)
        if len(u) == 4:
            el4_array = calc_array(u)
    aeg_array = el7_array - el4_array
    if aeg_array.sum() != 3:
        raise RuntimeError('missing value')
    return aeg_array

def find_ecd(all_segments):
    # ecd = 3*len7:abcdefg - (sum of tree 6)abcdfg:abdefg:abcefg
    for s in [1,4,7,8]:
        if not len(DIGITS[s]['txt']) in [len(u) for u in all_segments]:
            raise RuntimeError('missing value')
    el6_array = np.zeros(7)
    for u in all_segments:
        if len(u) == 7:
            el7_array = calc_array(u)
        if len(u) == 6:
            el6_array += calc_array(u)
    ecd_array = el7_array*3 - el6_array
    if ecd_array.sum() != 3:
        raise RuntimeError('missing value')
    return ecd_array

def find_7c(all_segments):
    # find len 6 without c
    for s in [1,4,7,8]:
        if not len(DIGITS[s]['txt']) in [len(u) for u in all_segments]:
            raise RuntimeError('missing value')
    el2_array = np.zeros(7)
    for u in all_segments:
        if len(u) == 2:
            el2_array = calc_array(u)
    
    for u in all_segments:
        if len(u) == 6:
            sample = calc_array(u)
            if (sample == el2_array).sum() == 1: # they only share 'f'
                el6c_array = sample
    if el6c_array.sum() != 6:
        raise RuntimeError('missing value')
    return el6c_array

def find_cebebf(all_segments):
    # cebebf = 3*len7:abcdefg - (sum of tree 5)abdfg:acdfg:acdeg
    for s in [1,4,7,8]:
        if not len(DIGITS[s]['txt']) in [len(u) for u in all_segments]:
            raise RuntimeError('missing value')
    el5_array = np.zeros(7, dtype=int)
    for u in all_segments:
        if len(u) == 7:
            el7_array = calc_array(u)
        if len(u) == 5:
            el5_array += calc_array(u)
    cebebf_array = el7_array*3 - el5_array
    if cebebf_array.sum() != 6:
        raise RuntimeError('missing value')
    return cebebf_array

def find_5be(all_segments):
    # ecd = 3*len7:abcdefg - (sum of tree 6)abcdfg:abdefg:abcefg
    for s in [1,4,7,8]:
        if not len(DIGITS[s]['txt']) in [len(u) for u in all_segments]:
            raise RuntimeError('missing value')
    el2_array = np.zeros(7)
    for u in all_segments:
        if len(u) == 2:
            el2_array = calc_array(u)
    
    for u in all_segments:
        if len(u) == 5:
            sample = calc_array(u)
            if (sample == el2_array).sum() == 2: # only one 5 length share cf with the 2 length
                el5be_array = sample
    if el5be_array.sum() != 5:
        raise RuntimeError('missing value')
    return el5be_array

class LineSegment():
    def __init__(self, line):
        io = [p.strip() for p in line.split('|')]
        self.input = InputSegment(["". join(sorted(p.strip())) for p in io[0].split(' ')])
        self.output = OutputSegment(["". join(sorted(p.strip())) for p in io[1].split(' ')])
        return
    def solve(self):
        # enc * x = correct Ax = B
        size = count_short(self.input.parts) + count_short(self.output.parts)
        
        unique_segments = list(set(get_short(self.input.parts) + get_short(self.output.parts)))
        all_segments = list(set((self.input.parts) + (self.output.parts)))
        array_enc = np.zeros((len(unique_segments)+8, 7))
        array_sol = np.zeros((len(unique_segments)+8, 7))
        i = 0
        for s in [1,4,7,8]:
            if not len(DIGITS[s]['txt']) in [len(u) for u in unique_segments]:
                raise RuntimeError('missing value')
        # DIGITS[1]['array']+DIGITS[7]['array'] the one with 1 is "a"
        for part in unique_segments:
            part_array = calc_array(part)
            array_enc[i, :] = part_array
            array_sol[i, :] = get_array_with_length(len(part))
            i += 1
        # find len=2 and len=3
        array_enc[i, :] = find_a(unique_segments)
        array_sol[i, :] = DIGITS2['acf'] - DIGITS2['cf']
        i += 1
        array_enc[i, :] = find_bf(unique_segments)
        array_sol[i, :] = DIGITS2['bcdf'] - DIGITS2['cf']
        i += 1
        array_enc[i, :] = find_aeg(unique_segments)
        array_sol[i, :] = DIGITS2['abcdefg'] - DIGITS2['bcdf']
        i += 1
        array_enc[i, :] = find_ecd(all_segments)
        array_sol[i, :] = DIGITS2['abcdefg']*3 - DIGITS2['abcdfg'] - DIGITS2['abdefg'] - DIGITS2['abcefg']
        i += 1
        array_enc[i, :] = find_cebebf(all_segments)
        array_sol[i, :] = DIGITS2['abcdefg']*3 - DIGITS2['abdfg'] - DIGITS2['acdfg'] - DIGITS2['acdeg']
        i += 1
        array_enc[i, :] = find_d(all_segments)
        array_sol[i, :] = DIGITS2['abcdefg'] - DIGITS2['abcefg']
        i += 1
        array_enc[i, :] = find_7c(all_segments)
        array_sol[i, :] = DIGITS2['abdefg']
        i += 1
        array_enc[i, :] = find_5be(all_segments)
        array_sol[i, :] = DIGITS2['acdfg']
        

        logging.info(array_enc)
        logging.info(array_sol)
        # x = array_sol * array_enc^-1
        convertor = (np.linalg.pinv(array_enc).dot(array_sol))
        convertor = np.around(convertor, 3)
        if not convertor.shape == (7,7):
            raise RuntimeError('wrong shape')
        check_array = np.around(array_enc.dot(convertor)).astype(int) == array_sol.astype(int)
        if check_array.all() != True:
            raise RuntimeError('solution not found')
        for seg in all_segments:
            part_array = calc_array(seg)
            con_part_array = np.around(part_array.dot(convertor)).astype(int)
            dig = 'F'
            for k in DIGITS.keys():
                if (DIGITS[k]['array'].astype(int) == con_part_array).all():
                    dig = str(k)
            if dig == 'F':
                raise RuntimeError('did not decode correcy')
        return convertor
    def calc_output(self) -> int:
        result = []
        conv = self.solve()
        for part in self.output.parts:
            part_array = calc_array(part)
            con_part_array = np.around(part_array.dot(conv)).astype(int)
            dig = 'F'
            for k in DIGITS.keys():
                if (DIGITS[k]['array'].astype(int) == con_part_array).all():
                    dig = str(k)
            if dig == 'F':
                raise RuntimeError('did not decode correcy')
            result.append(dig)
        return int("".join(result))


class day8_tasks(object):
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
            lines = [line.strip() for line in _f.readlines()]
            # 9,4 -> 3,4
        for line in lines:
            self.line_segments.append(LineSegment(line))
        return
    def solve(self):
        fail = False
        for line in self.line_segments:
            line.solve()
        return fail == False
    def calc(self) -> int:
        count = 0
        for segment in self.line_segments:
            count += count_short(segment.output.parts)
        return count
    def calc_output_value(self) -> int:
        count = 0
        for segment in self.line_segments:
            # logging.info("known segments input:{}, output:{}".format(count_short(segment.input.parts), count_short(segment.output.parts)))
            count += segment.calc_output()
        return count

if __name__ == '__main__':
    file = 'resource/dataset_test.csv'
    run = day8_tasks(file)
    run.calc()
    run.calc_complex()


