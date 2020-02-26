import cv2

image = cv2.imread("Lena.png", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Original Image", image)

for y in range(0, image.shape[0]):
    for x in range(1, int(image.shape[1])):
        image[y, x] = 0 if image[y, x] < 180 else 255

cv2.imshow("Modified Image", image)
cv2.waitKey(0)
