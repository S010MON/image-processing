import numpy as np


def histogram(img):
    img = img[:, :, 1]

    data = []
    for line in img:
        for pixel in line:
            data.append(pixel)

    return data


def negative(img):
    return 255 - int(img)


def contrast(img, gamma):
    img = np.divide(img, 255)
    return np.power(img, 1/gamma)

