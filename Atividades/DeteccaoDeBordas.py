import cv2 as cv
import numpy as np

capture = cv.VideoCapture("videos\catVideo.mp4")

while True:
    isTrue, frame = capture.read()
    cv.imshow('Worlds Smallest Cat', frame)

    bordas = cv.Canny(frame, 100, 100)
    cv.imshow('Canny', bordas)

    laplace = cv.Laplacian(frame, cv.CV_64F)
    laplace = np.uint8(laplace)
    cv.imshow('laplace', laplace)

    if cv.waitKey(20) & 0xFF == ord('b'):
        break

capture.release()
cv.destroyAllWindows()