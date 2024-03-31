import unittest
from main import nearest_neighbor

class TestNearestNeighbor(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(nearest_neighbor([], (0, 0)))

    def test_single_point(self):
        self.assertEqual(nearest_neighbor([(1, 1)], (0, 0)), (1, 1))

    def test_multiple_points(self):
        points = [(1, 1), (2, 2), (3, 3)]
        self.assertEqual(nearest_neighbor(points, (0, 0)), (1, 1))

    def test_point_at_same_location(self):
        points = [(1, 1), (2, 2), (3, 3)]
        self.assertEqual(nearest_neighbor(points, (1, 1)), (1, 1))

if __name__ == '__main__':
    unittest.main()