import cv2 as cv

img = cv.imread('imagens\TwoCats.jpeg')
cv.imshow("Cats", img)

# Avaraging Blur
average = cv.blur(img, (5, 5))
cv.imshow("Average Blurred Cats", average)

cv.waitKey(0)
cv.destroyAllWindows()
