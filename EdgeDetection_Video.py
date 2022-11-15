import cv2
import numpy as np
from matplotlib import pyplot as plt

vid = cv2.VideoCapture("Media/Test1.mp4")

while (vid.isOpened()):
    ret, frame = vid.read()
    #scaled frame dimensions: 378x504
    frame = cv2.resize(frame, (756, 1008), fx = 0, fy = 0, interpolation = cv2.INTER_CUBIC)
    #frame.astype(np.uint8)
    originalWidth = frame.shape[1]
    originalHeight = frame.shape[0]
    x1 = int(originalWidth*(68/128))
    x2 = int(originalWidth*(70/128))
    y1 = int(originalHeight*(4/8))
    y2 = int(originalHeight*(5/8))

    cropped_frame = frame[y1:y2, x1:x2]
    frameEdges = cv2.Canny(cropped_frame, 50, 200)
    cv2.imshow('Frame', frame)
    cv2.imshow('New_Frame', frameEdges)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()