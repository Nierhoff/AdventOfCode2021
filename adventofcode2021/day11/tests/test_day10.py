import unittest
from adventofcode2021.day10.tasks.day10_tasks import day10_tasks
import numpy as np

class Test_test_day10(unittest.TestCase):

    def test_task1_syntax_error_score(self):
        t1 = day10_tasks('resource/dataset_test.csv')
        actual = t1.calc_syntax_error_score()
        expected = 0
        self.assertEqual(actual, expected, 'Wrong result')
        return

if __name__ == '__main__':
    unittest.main()
