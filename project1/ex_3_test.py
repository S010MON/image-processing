import unittest
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

    def test_cart_to_polar_x(self):
        v = (1, 0)
        exp = (1, 0)
        act = polar(v)
        self.assertEqual(exp, act)

    def test_polar_to_cartesian_x(self):
        v = (1, 0)
        exp = (1, 0)
        act = carteisan(v)
        self.assertEqual(exp, act)

    def test_cart_to_polar_y(self):
        v = (0, 1)
        exp = (0, 1)
        act = polar(v)
        self.assertEqual(exp, act)

    def test_polar_to_cartesian_y(self):
        v = (0, 1)
        exp = (0, 1)
        act = carteisan(v)
        self.assertEqual(exp, act)

    def test_cart_to_polar_both(self):
        v = (5.0, 10.0)
        exp = (11.18, 1.107)
        act = polar(v)
        self.assertAlmostEqual(exp[0], act[0], delta=0.1)
        self.assertAlmostEqual(exp[1], act[1], delta=0.1)

    def test_polar_to_cartesian_both(self):
        v = (5.0, 10.0)
        exp = (-4.195, -2.720)
        act = carteisan(v)
        self.assertAlmostEqual(exp[0], act[0], delta=0.1)
        self.assertAlmostEqual(exp[1], act[1], delta=0.1)


if __name__ == '__main__':
    unittest.main()
