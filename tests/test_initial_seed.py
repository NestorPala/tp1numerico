import unittest
from main import initial_seed


class InitialSeedTestCase(unittest.TestCase):
    def test_n_equal_to_4(self):
        n = 4
        self.assertEqual([0, 0, 0, 0, 0, 0, 0, 0, 0], initial_seed(n))

    def test_n_equal_to_3(self):
        n = 3
        self.assertEqual([0, 0, 0, 0], initial_seed(n))

    def test_n_equal_to_2(self):
        n = 2
        self.assertEqual([0], initial_seed(n))


if __name__ == '__main__':
    unittest.main()
