import cv2
import matplotlib.pyplot as plt


def histogram(img):
    img = img[:,:,1]

    data = dict()
    for line in img:
        for pixel in line:
            if pixel not in data:
                data[pixel] = 1
            else:
                data[pixel] += 1

    plt.hist(data.values())
    plt.show()


if __name__ == '__main__':
    img1 = cv2.imread('images/fog.jpg')
    histogram(img1)
    img2 = cv2.imread('images/shadows.jpg')
    histogram(img2)
