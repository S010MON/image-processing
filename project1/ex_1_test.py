import unittest
import cv2
from ex_1 import rgb_to_hsv, rgb2hsv


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

    def test_ex_1(self):
        img_bgr = cv2.imread('images/falafel.png')
        img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
        exp = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2HSV)
        act = rgb2hsv(img_rgb)
        for x in range(len(exp)):
            for y in range(len(exp[x])):
                for z in range(len(exp[x][y])):
                    self.assertAlmostEqual(exp[x][y][z], act[x][y][z], delta=0.1)


if __name__ == '__main__':
    unittest.main()
