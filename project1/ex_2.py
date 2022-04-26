import cv2
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


def contrasts(img_path: str):

    img = cv2.imread(img_path)
    cv2.imshow('Original', img)
    cv2.imshow('Negative', negative(img))
    cv2.imshow('Low Contrast', contrast(img, 1.5))
    cv2.imshow('High Contrast', contrast(img, 0.5))
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    contrasts('images/fog_small.png')
    contrasts('images/shadows_small.png')
