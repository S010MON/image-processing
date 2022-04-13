import cv2


# Colour Spaces
import numpy as np


def rgb_to_hsv(r: int, g: int, b: int) -> tuple:
    r = r / 255
    g = g / 255
    b = b / 255

    v = max(r, g, b)
    c = v - min(r, g, b)
    if v == 0:
        s = 0
    else:
        s = c / v

    if c == 0:
        h = 0.0
    elif v == r:
        h = 60 * (0 + (g - b) / c)
    elif v == g:
        h = 60 * (2 + (b - r) / c)
    else:
        h = 60 * (4 + (r - g) / c)

    h = (h + 360) % 360
    s = s * 100
    v = v * 100

    return h, s, v


img_bgr = cv2.imread('falafel.png')
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
img_hsv = np.ones(np.shape(img_rgb))

print(f"x = {len(img_rgb)}")
print(f"y = {len(img_rgb[0])}")
print(f"y = {len(img_rgb[0][0])}")

for x in range(len(img_rgb)):
    for y in range(len(img_rgb[0])):
        r = img_rgb[x][y][0]
        g = img_rgb[x][y][1]
        b = img_rgb[x][y][2]
        h, s, v = rgb_to_hsv(r, g, b)
        img_hsv[x][y][0] = h
        img_hsv[x][y][1] = s
        img_hsv[x][y][2] = v


cv2.imshow('rgb', img_rgb)
cv2.imshow('hsv', img_hsv)

cv2.waitKey(0)
cv2.destroyAllWindows()