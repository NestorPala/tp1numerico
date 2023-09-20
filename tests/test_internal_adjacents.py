import unittest
from main import internal_adjacents


class InternalAdjacentsTestCase(unittest.TestCase):

    """
    [
        [3,6,9],
        [2,5,8],
        [1,4,7]
    ]
    """
    def test_n_equal_to_4(self):
        n = 4
        self.assertEqual([2, 4], internal_adjacents(z=1, n=n))
        self.assertEqual([1, 3, 5], internal_adjacents(z=2, n=n))
        self.assertEqual([2, 6], internal_adjacents(z=3, n=n))
        self.assertEqual([1, 5, 7], internal_adjacents(z=4, n=n))
        self.assertEqual([2, 4, 6, 8], internal_adjacents(z=5, n=n))
        self.assertEqual([3, 5, 9], internal_adjacents(z=6, n=n))
        self.assertEqual([4, 8], internal_adjacents(z=7, n=n))
        self.assertEqual([5, 7, 9], internal_adjacents(z=8, n=n))
        self.assertEqual([6, 8], internal_adjacents(z=9, n=n))

    """
    [
        [2,4],
        [1,3]
    ]
    """
    def test_n_equal_to_3(self):
        n = 3
        self.assertEqual([2, 3], internal_adjacents(z=1, n=n))
        self.assertEqual([1, 4], internal_adjacents(z=2, n=n))
        self.assertEqual([1, 4], internal_adjacents(z=3, n=n))
        self.assertEqual([2, 3], internal_adjacents(z=4, n=n))

    # [1]
    def test_n_equal_to_2(self):
        n = 2
        self.assertEqual([], internal_adjacents(z=1, n=n))


if __name__ == '__main__':
    unittest.main()
