import unittest
from functions import rgb_to_hsv


class MyTestCase(unittest.TestCase):
    def test_rgb_hsv_black(self):
        rgb = (0, 0, 0)
        exp = (0, 0, 0)
        act = rgb_to_hsv(rgb[0], rgb[1], rgb[2])
        for i in range(len(exp)):
            self.assertAlmostEqual(exp[i], act[i], delta=0.1)

    def test_rgb_hsv_white(self):
        rgb = (255, 255, 255)
        exp = (0, 0, 1)
        act = rgb_to_hsv(rgb[0], rgb[1], rgb[2])
        for i in range(len(exp)):
            self.assertAlmostEqual(exp[i], act[i], delta=0.1)

    def test_rgb_hsv_red(self):
        rgb = (255, 0, 0)
        exp = (0, 1, 1)
        act = rgb_to_hsv(rgb[0], rgb[1], rgb[2])
        for i in range(len(exp)):
            self.assertAlmostEqual(exp[i], act[i], delta=0.1)

    def test_rgb_hsv_green(self):
        rgb = (0, 255, 0)
        exp = (120, 1, 1)
        act = rgb_to_hsv(rgb[0], rgb[1], rgb[2])
        for i in range(len(exp)):
            self.assertAlmostEqual(exp[i], act[i], delta=0.1)

    def test_rgb_hsv_blue(self):
        rgb = (0, 0, 255)
        exp = (240, 1, 1)
        act = rgb_to_hsv(rgb[0], rgb[1], rgb[2])
        for i in range(len(exp)):
            self.assertAlmostEqual(exp[i], act[i], delta=0.1)

    def test_rgb_hsv_rand(self):
        rgb = (35, 60, 68)
        exp = (195, 0.49, 0.27)
        act = rgb_to_hsv(rgb[0], rgb[1], rgb[2])
        for i in range(len(exp)):
            self.assertAlmostEqual(exp[i], act[i], delta=0.5)


if __name__ == '__main__':
    unittest.main()
