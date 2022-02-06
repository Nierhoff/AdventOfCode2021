import unittest
from adventofcode2021.day7.tasks.day7_tasks import day7_tasks
import numpy as np

class Test_test_day6(unittest.TestCase):

    def test_task1_position(self):
        t1 = day7_tasks('resource/dataset_test.csv')
        actual = t1.get_position()
        expected = 2
        self.assertEqual(actual, expected, 'Wrong result')
        return
    def test_task1_fuel(self):
        t1 = day7_tasks('resource/dataset_test.csv')
        actual = t1.calc()
        expected = 37
        self.assertEqual(actual, expected, 'Wrong result')
        return
    def test_task1_fuel_real(self):
        t1 = day7_tasks('resource/dataset.csv')
        actual = t1.calc()
        expected = 344605
        self.assertEqual(actual, expected, 'Wrong result')
        return
    def test_task2_fuel(self):
        t1 = day7_tasks('resource/dataset_test.csv')
        actual = t1.calc_progresive()
        expected = 168
        self.assertEqual(actual, expected, 'Wrong result')
        return
    def test_task2_fuel_real(self):
        t1 = day7_tasks('resource/dataset.csv')
        actual = t1.calc_progresive()
        expected = 93699985
        self.assertEqual(actual, expected, 'Wrong result')
        return

if __name__ == '__main__':
    unittest.main()
