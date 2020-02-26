import cv2

image = cv2.imread("Lena.png", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Original Image", image)

height, width = image.shape

for i in range(width):
    for j in range(height):
        image[j, i] = 255 - image[j, i]

cv2.imshow("Modified Image", image)
cv2.waitKey(0)
