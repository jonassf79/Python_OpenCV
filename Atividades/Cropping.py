import cv2 as cv
import numpy as np

img = cv.imread('Semana1_EstudosOpenCV\\imagens\\cat.jpg')
cv.imshow("padrão", img)

# Cropping
cropped = img[300:500, 200:400]  # 200x200
cv.imshow("cropped", cropped)

cv.waitKey(0)
cv.destroyAllWindows()

