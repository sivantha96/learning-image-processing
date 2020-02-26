import numpy as np
import cv2
import matplotlib.pyplot as plt

image = cv2.imread("lena_color.png", cv2.IMREAD_GRAYSCALE)
cv2.imshow("original image", image)

height, width = image.shape
values = []

for i in range(width):
    for j in range(height):
        values.append(image[i, j])

histogram =np.histogram(values)

plt.hist(histogram)
plt.show(Test1.py)
cv2.waitKey(0)