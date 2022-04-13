import cv2


img_rgb = cv2.imread('pizza1.png')

cv2.imshow('image', img_rgb)

cv2.waitKey(0)
cv2.destroyAllWindows()
