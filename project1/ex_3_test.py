import unittest
import cv2
from ex_3 import carteisan, polar


class MyTestCase(unittest.TestCase):

    def test_cart_to_polar_zero(self):
        v = (0, 0)
        exp = (0, 0)
        act = polar(v)
        self.assertEqual(exp, act)

    def test_polar_to_cartesian_zero(self):
        v = (0, 0)
        exp = (0, 0)
        act = carteisan(v)
        self.assertEqual(exp, act)


if __name__ == '__main__':
    unittest.main()
