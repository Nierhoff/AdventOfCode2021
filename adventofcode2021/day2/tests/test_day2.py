import unittest
from adventofcode2021.day2.tasks.day2_tasks import day2_tasks

class Test_test_day2(unittest.TestCase):
    def test_task1(self):
        t1 = day2_tasks('resource/dataset_test.csv')
        actual = t1.calc()
        expected = 150
        self.assertEqual(actual, expected, 'Wrong result')
        return

    def test_task1_real(self):
        t1 = day2_tasks('resource/dataset.csv')
        actual = t1.calc()
        expected = 1484118
        self.assertEqual(actual, expected, 'Wrong result')
        return

    def test_task2(self):
        t2 = day2_tasks('resource/dataset_test.csv')
        actual = t2.calc_complex()
        expected = 900
        self.assertEqual(actual, expected, 'Wrong result')
        return

    def test_task2_real(self):
        t2 = day2_tasks('resource/dataset.csv')
        actual = t2.calc_complex()
        expected = 1463827010
        self.assertEqual(actual, expected, 'Wrong result')
        return


if __name__ == '__main__':
    unittest.main()
