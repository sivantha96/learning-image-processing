import cv2

image = cv2.imread("Lena.png", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Original Image", image)

height, width = image.shape

for y in range(0, image.shape[0]):
    for x in range(0, image.shape[1]):
        i = image[y, width-x]
        image[y, width-x] = image[y, x]
        image[y, x] = x

cv2.imshow("Modified Image", image)
cv2.waitKey(0)
