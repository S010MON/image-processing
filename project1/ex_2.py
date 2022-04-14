import cv2
import matplotlib.pyplot as plt
import numpy as np


def histogram(img):
    img = img[:,:,1]

    data = []
    for line in img:
        for pixel in line:
            data.append(pixel)

    return data


def pointwise(img):

    img_out = np.zeros(np.shape(img))
    for x in range(len(img)):
        for y in range(len(img[x])):

            s = 100 - 1 - img[x][y][0]
            img_out[x][y][0] = s
            img_out[x][y][1] = s
            img_out[x][y][2] = s

    return img_out


if __name__ == '__main__':
    img1 = cv2.imread('images/shadows_small.png')
    neg1 = pointwise(img1)

    img2 = cv2.imread('images/fog_small.png')
    neg2 = pointwise(img2)

    data_img1 = histogram(img1)
    data_neg1 = histogram(neg1)
    data_img2 = histogram(img2)
    data_neg2 = histogram(neg2)

    plt.subplot(2, 2, 1)
    plt.hist(data_img1, bins=255)
    plt.title('Shadows Greyscale')

    plt.subplot(2, 2, 2)
    plt.title('Shadows Negative')
    plt.hist(data_neg1, bins=255)

    plt.subplot(2, 2, 3)
    plt.title('Fog Greyscale')
    plt.hist(data_img2, bins=255)

    plt.subplot(2, 2, 4)
    plt.title('Fog Negative')
    plt.hist(data_neg2, bins=255)
    plt.show()

    cv2.imshow('Original', img1)
    cv2.imshow('Negative', neg1)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
