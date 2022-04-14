import cv2
import numpy as np


def rgb2hsv(img_rgb):

    img_hsv = np.ones(np.shape(img_rgb))

    for x in range(len(img_rgb)):
        for y in range(len(img_rgb[0])):
            r = img_rgb[x][y][0]
            g = img_rgb[x][y][1]
            b = img_rgb[x][y][2]
            h, s, v = rgb_to_hsv(r, g, b)
            img_hsv[x][y][0] = h
            img_hsv[x][y][1] = s
            img_hsv[x][y][2] = v

    return img_hsv


def rgb_to_hsv(r: int, g: int, b: int) -> tuple:
    # source: https://docs.opencv.org/4.x/de/d25/imgproc_color_conversions.html#color_convert_rgb_hsv

    r = r / 255
    g = g / 255
    b = b / 255

    v = max(r, g, b)
    c = (v - min(r, g, b))

    if v != 0:
        s = c / v
    else:
        s = 0

    if r == g == b:
        h = 0
    elif v == r:
        h = (60 * (g - b)) / c
    elif v == g:
        h = 120 + 60 * (b - r) / c
    elif v == b:
        h = 240 + 60 * (r - g) / c

    if h < 0:
        h = h + 360

    return h, s, v


def rgb2hsi(img_rgb):

    img_hsi = np.ones(np.shape(img_rgb))

    for x in range(len(img_rgb)):
        for y in range(len(img_rgb[0])):
            r = img_rgb[x][y][0]
            g = img_rgb[x][y][1]
            b = img_rgb[x][y][2]
            h, s, v = rgb_to_hsi(r, g, b)
            img_hsi[x][y][0] = h
            img_hsi[x][y][1] = s
            img_hsi[x][y][2] = v

    return img_hsi


def rgb_to_hsi(r: int, g: int, b: int) -> tuple:
    r = r / 255
    g = g / 255
    b = b / 255

    v = max(r, g, b)
    c = v - min(r, g, b)
    if v == 0:
        s = 0
    else:
        s = 1 - (min(r, g, b) / ((r + b + g)/3))

    if c == 0:
        h = 0.0
    elif v == r:
        h = 60 * (0 + (g - b) / c)
    elif v == g:
        h = 60 * (2 + (b - r) / c)
    else:
        h = 60 * (4 + (r - g) / c)

    h = (h + 360) % 360

    return h, s, v


if __name__ == '__main__':
    img1_rgb = cv2.imread('images/falafel.png')
    img1_hsv = rgb2hsv(img1_rgb)
    img1_hsi = rgb2hsi(img1_rgb)

    cv2.imshow('rgb1', img1_rgb)
    cv2.imshow('hsv1', img1_hsv)
    cv2.imshow('hsi1', img1_hsi)

    img2_rgb = cv2.imread('images/beach.png')
    img2_hsv = rgb2hsv(img2_rgb)
    img2_hsi = rgb2hsi(img2_rgb)

    cv2.imshow('rgb2', img2_rgb)
    cv2.imshow('hsv2', img2_hsv)
    cv2.imshow('hsi2', img2_hsi)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
