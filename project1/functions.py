import numpy as np
import cv2

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


def histogram(img):
    img = img[:, :, 1]

    data = []
    for line in img:
        for pixel in line:
            data.append(pixel)

    return data


def contrast(img, gamma):
    img = np.divide(img, 255)
    return np.power(img, 1/gamma)


def polar(img):
    value = np.sqrt(((img.shape[0] / 2.0) ** 2.0) + ((img.shape[1] / 2.0) ** 2.0))
    polar_image = cv2.linearPolar(img, (img.shape[0] / 2, img.shape[1] / 2), value, cv2.WARP_FILL_OUTLIERS)
    return polar_image.astype(np.uint8)


def cartoonify(img, K):
    # https://medium.com/nerd-for-tech/cartoonize-images-with-python-10e2a466b5fb

    img_gb = cv2.GaussianBlur(img, (7, 7), 0)                                   # Apply some Gaussian blur on the image
    img_mb = cv2.medianBlur(img_gb, 5)                                          # Apply some Median blur on the image
    img_bf = cv2.bilateralFilter(img_mb, 5, 80, 80)                             # Apply a bilateral filer on the image

    img_lp_al = cv2.Laplacian(img_bf, cv2.CV_8U, ksize=5)                       # Use the laplace filter to detect edges
    img_lp_al_grey = cv2.cvtColor(img_lp_al, cv2.COLOR_BGR2GRAY)                # Convert the image to greyscale (1D)
    _, EdgeImage = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)              # Manual image thresholding
    blur_al = cv2.GaussianBlur(img_lp_al_grey, (5, 5), 0)                       # Remove some additional noise
    _, tresh_al = cv2.threshold(blur_al, 245, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)     # Apply a threshold (Otsu)
    inverted_Bilateral = cv2.subtract(255, tresh_al)                            # Invert the black and the white
    img_reshaped = img.reshape((-1, 3))                                         # Reshape the image
    img_reshaped = np.float32(img_reshaped)                                     # convert to np.float32

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)    # Set the Kmeans criteria
    _, label, center = cv2.kmeans(img_reshaped, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    div = 32
    img_bins = img // div * div + div // 2
    inverted_Bilateral = cv2.cvtColor(inverted_Bilateral, cv2.COLOR_GRAY2RGB)   # Convert the mask image back to color

    combined = cv2.bitwise_and(inverted_Bilateral, img_bins)                    # Combine the edge image and the binned image
    return (inverted_Bilateral, img_bins, combined)

