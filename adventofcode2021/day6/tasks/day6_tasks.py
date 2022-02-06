import logging # https://docs.python.org/3/howto/logging.html
import sys
import os.path
import numpy as np

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

DIR_PATH: str = os.path.dirname(os.path.realpath(__file__))

class LanternFish():
    def __init__(self, time: int, age=0) -> None:
        self.time: int = int(time)
        self.age: int = int(age)
        return
    def run(self):
        if self.time == 0:
            fish = [LanternFish(6, self.age), LanternFish(8)]
        else:
            self.time -= 1
            fish = [self]
        self.age += 1
        return fish

class LanternFishGroup():
    def __init__(self, time: int, number: int) -> None:
        self.time: int = int(time)
        self.number: int = int(number)
        return
    def increase_number(self, number):
        self.number += number
        return
    def __add__(self, other):
        if self.time == other.time:
            self.increase_number(other.number)
        else:
            raise RuntimeError('not able to add')
        return self
    def __gt__(self, other):
        return self.time > other.time
    def __lt__(self, other):
        return self.time < other.time

class LanternFishGroups():
    def __init__(self) -> None:
        self.groups: List[LanternFishGroup] = list()
        self.age: int = 0
        return
    def add_group(self, group):
        self.groups.append(group)
        return
    def get_group(self, time: int):
        result = None
        for group in self.groups:
            if group.time == time:
                result = group
        if result == None:
            result = LanternFishGroup(time, 0)
            self.groups.append(result)
        return result
    def run(self):
        new_groups = []
        for group in self.groups:
            if group.time == 0:
                group.time = 6
                new_groups.append(LanternFishGroup(8, int(group.number)))
            else:
                group.time -= 1
        self.age += 1
        for new_group in new_groups:
            group = self.get_group(new_group.time)
            group.increase_number(new_group.number)
        return
    def sum(self) -> int:
        number = 0
        for group in self.groups:
            number += group.number
        return number


class day6_tasks(object):
    """description of class"""

    def __init__(self, file: str) -> None:
        self.file = None
        self.initial = []
        self.fishlist = {}
        self.age = 0
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
            self.initial = list(np.genfromtxt(_f, dtype=int, delimiter=','))
        self.fish = LanternFishGroups()
        for time in range(0, max(self.initial)+1):
            number = self.initial.count(time)
            self.fish.add_group(LanternFishGroup(time, number))
        self.set_status()
        return
    def set_status(self):
        self.fishlist[int(self.fish.age)] =  int(self.fish.sum())
        return
    def run(self):
        self.fish.run()
        self.set_status()
        self.age = self.fish.age
        logging.info('At day ' + str(self.fish.age) + ' there is ' + str(self.fishlist[self.fish.age]) + ' fish' )
        return self.fish
    def runs(self, days=0):
        while self.age < days:
            self.run()
    def calc_18(self):
        day = 18
        self.runs(day)
        return self.fishlist[day]
    def calc_80(self):
        day = 80
        self.runs(day)
        return self.fishlist[day]
    def calc_256(self):
        day = 256
        self.runs(day)
        return self.fishlist[day]

if __name__ == '__main__':
    file = 'resource/dataset_test.csv'
    run = day6_tasks(file)
    run.calc()
    run.calc_complex()


