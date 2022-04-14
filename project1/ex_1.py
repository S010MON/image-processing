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
        h = 60 * ((g - b) / c)
    elif v == g:
        h = 120 + (60 * (b - r) / c)
    elif v == b:
        h = 240 + (60 * (r - g) / c)

    if h < 0:
        h = h + 360

    return h/255/2, s, v


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
    c = (v - min(r, g, b))

    if v != 0:
        s = c / v
    else:
        s = 0

    if r == g == b:
        h = 0
    elif v == r:
        h = 60 * ((g - b) / c)
    elif v == g:
        h = 120 + (60 * (b - r) / c)
    elif v == b:
        h = 240 + (60 * (r - g) / c)

    if h < 0:
        h = h + 360

    i = (r + b + g) / 3

    return h/255/2, s, i


if __name__ == '__main__':
    img_rgb = cv2.imread('images/falafel.png')
    img_hsv_act = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2HSV)
    img_hsv_own = rgb2hsv(img_rgb)
    img_hsi_own = rgb2hsi(img_rgb)

    cv2.imshow('rgb', img_rgb)
    cv2.imshow('hsv act', img_hsv_act)
    cv2.imshow('hsv own', img_hsv_own)
    cv2.imshow('hsi own', img_hsi_own)


    cv2.waitKey(0)
    cv2.destroyAllWindows()
