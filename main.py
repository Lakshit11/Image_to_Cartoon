import cv2
import numpy as np

# reading the image
img = cv2.imread('img.jpg')

# converting image into gray scale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)

# identifying edges for the image
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

# coloring the gray part
color = cv2.bilateralFilter(img, 9, 250, 250)

# cartoonizing the image
cartoon = cv2.bitwise_and(color, color, mask = edges)

# displaying image
cv2.imshow("Cartoon", cartoon)

cv2.waitKey(0)
cv2.destroyAllWindows()
