import math
import cv2
import numpy as np


def polar(coordinate: tuple) -> tuple:
    x = coordinate[0]
    y = coordinate[1]
    r = math.sqrt(x**2 + y**2)
    theta = math.atan2(y, x)
    return r, theta


def carteisan(coordinate: tuple) -> tuple:
    r = coordinate[0]
    theta = coordinate[1]
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return x, y


def pad_img(img):
    return np.pad(img, ((10, 10), (10, 10), (0, 0)), constant_values=True)


def cartoonify_2(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
    return img


if __name__ == '__main__':
    img = cv2.imread('images/door_small.png')
    cv2.imshow('Cartesian', img)

    value = np.sqrt(((img.shape[0] / 2.0) ** 2.0) + ((img.shape[1] / 2.0) ** 2.0))
    polar_image = cv2.linearPolar(img, (img.shape[0] / 2, img.shape[1] / 2), value, cv2.WARP_FILL_OUTLIERS)
    polar_image = polar_image.astype(np.uint8)
    cv2.imshow("Polar", polar_image)

    """
    The canny edge detector is the edge detection operation that operates on multi-stage algorithms to detect a wide 
    range of edges in the image. The process involves: applies the Gaussian filter to a smooth image, finds the 
    intensity gradient of the image, applies gradient magnitude thresholding to get rid of spurious response to edge 
    detection, applies a double threshold to determine potential edges, and tracks the edges by hysteresis.        
    """

    img_modifed = cv2.Canny(img, 100, 200)
    cv2.imshow("Cartoonify", img_modifed)
    cv2.imshow("Cartoonify 2", cartoonify_2(img))

    cv2.waitKey(0)
    cv2.destroyAllWindows()
