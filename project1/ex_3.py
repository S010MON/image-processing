import math


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


if __name__ == '__main__':
    img = cv2.imread('images/')