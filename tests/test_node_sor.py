import unittest
from main import node_sor, UPPER, LOWER, LEFT, RIGHT


class NodeSORTestCase(unittest.TestCase):

    def test_n_equal_to_4_and_z_equal_to_1(self):
        z = 1
        n = 4
        x1 = []
        x0 = [12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5]
        w = 1.5
        boundaries = [-1, -1, -1, -1]
        boundaries[UPPER] = 15.0
        boundaries[LOWER] = 15.0
        boundaries[LEFT] = 20.0
        boundaries[RIGHT] = 20.0
        self.assertEqual(17.75, node_sor(z, n, x1, x0, w, boundaries))

    def test_n_equal_to_4_and_z_equal_to_5(self):
        z = 5
        n = 4
        x1 = [12.0, 13.0, 14.0, 15.0]
        x0 = [12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5]
        w = 1.5
        boundaries = [-1, -1, -1, -1]
        boundaries[UPPER] = 15.0
        boundaries[LOWER] = 15.0
        boundaries[LEFT] = 20.0
        boundaries[RIGHT] = 20.0
        self.assertEqual(16.125, node_sor(z, n, x1, x0, w, boundaries))

    def test_n_equal_to_4_and_z_equal_to_6(self):
        z = 6
        n = 4
        x1 = [12.0, 13.0, 14.0, 15.0, 16.0]
        x0 = [12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5]
        w = 1.5
        boundaries = [-1, -1, -1, -1]
        boundaries[UPPER] = 15.0
        boundaries[LOWER] = 15.0
        boundaries[LEFT] = 20.0
        boundaries[RIGHT] = 20.0
        self.assertEqual(15.8125, node_sor(z, n, x1, x0, w, boundaries))


if __name__ == '__main__':
    unittest.main()
