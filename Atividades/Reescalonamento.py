import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    # Funciona com imagens, vídeos e vídeos em tempo real.
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width,height):
    # Somente funciona video em tempo real.
    capture.set(3,width)
    capture.set(4,height)

capture = cv.VideoCapture("EstudosOpenCV\videos\catVideo.mp4")

while True:
  isTrue, frame = capture.read()

  frame_resized = rescaleFrame(frame, scale=.2)
  
  cv.imshow('Worlds Smallest Cat' , frame_resized)

  if cv.waitKey(20) & 0xFF==ord('b'):
    break

capture.release()
cv.destroyAllWindows()
    
cv.waitKey(0)