import cv2
import matplotlib.pyplot as plt
import numpy as np


def histogram(img):
    img = img[:, :, 1]

    data = []
    for line in img:
        for pixel in line:
            data.append(pixel)

    return data


def negative(img):
    return 255 - img


def contrast(img, gamma):

    img = np.divide(img, 255)
    return np.power(img, 1/gamma)


if __name__ == '__main__':
    img1 = cv2.imread('images/shadows_small.png')
    img2 = cv2.imread('images/fog_small.png')

    data_img1 = histogram(img1)
    data_neg1 = histogram(negative(img1))
    data_img2 = histogram(img2)
    data_neg2 = histogram(negative(img2))

    # plt.subplot(2, 2, 1)
    # plt.hist(data_img1, bins=255)
    # plt.title('Shadows Greyscale')
    #
    # plt.subplot(2, 2, 2)
    # plt.title('Shadows Negative')
    # plt.hist(data_neg1, bins=255)
    #
    # plt.subplot(2, 2, 3)
    # plt.title('Fog Greyscale')
    # plt.hist(data_img2, bins=255)
    #
    # plt.subplot(2, 2, 4)
    # plt.title('Fog Negative')
    # plt.hist(data_neg2, bins=255)
    # plt.show()

    cv2.imshow('Original', img1)
    cv2.imshow('Negative', negative(img1))
    cv2.imshow('Low Contrast', contrast(img1, 1.7))
    cv2.imshow('High Contrast', contrast(img1, 0.3))

    cv2.waitKey(0)
    cv2.destroyAllWindows()
