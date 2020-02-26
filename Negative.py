import cv2

image = cv2.imread("Lena.png", cv2.IMREAD_COLOR)
cv2.imshow("Original Image", image)

for y in range(0, image.shape[0]):
    for x in range(0, int(image.shape[1]/2)):
        image[y, x] = (255, 255, 255) - image[y, x]

cv2.imshow("Modified Image", image)
cv2.waitKey(0)
