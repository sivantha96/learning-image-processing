import cv2

image = cv2.imread("Lena.png", cv2.IMREAD_COLOR)
cv2.imshow("Original Image", image)

for y in range(0, image.shape[0]):
    for x in range(1, int(image.shape[1])):
        i = image[y, x, 2]
        image[y, x, 2] = image[y, x, 0]
        image[y, x, 0] = i

cv2.imshow("Modified Image", image)
cv2.waitKey(0)
