import cv2 as cv

#Leitura de imagem:

#img = cv.imread('Semana1_EstudosOpenCV\imagens\cat.jpg')
#cv.imshow('Cat', img)

#cv.waitKey(0)

#Leitura de Vídeo:

capture = cv.VideoCapture("EstudosOpenCV\\videos\\catVideo.mp4")

while True:
    isTrue, frame = capture.read()
    cv.imshow('Worlds Smallest Cat', frame)

    if cv.waitKey(20) & 0xFF == ord('b'):
        break

capture.release()
cv.destroyAllWindows()