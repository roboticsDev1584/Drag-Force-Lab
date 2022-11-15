import cv2
import numpy as np
from matplotlib import pyplot as plt
from datetime import datetime

vid = cv2.VideoCapture("Media/Test7.mp4")
firstTime = True
secondTime = False

while (vid.isOpened()):
    if (firstTime):
        ret, frame = vid.read()
        frame = cv2.resize(frame, (270, 480), fx = 0, fy = 0, interpolation = cv2.INTER_CUBIC)
        originalWidth = frame.shape[1]
        originalHeight = frame.shape[0]

        xpos1 = int(originalWidth*(78/128))
        ypos1 = int(originalHeight*(75/128))
        cv2.circle(frame, (xpos1, ypos1), 2, (0, 0, 255), -1)
        print("pos1: "+str(xpos1)+", "+str(ypos1))

        xpos2 = int(originalWidth*(82/128))
        ypos2 = int(originalHeight*(78/128))
        cv2.circle(frame, (xpos2, ypos2), 2, (0, 0, 255), -1)
        print("pos2: "+str(xpos2)+", "+str(ypos2))

        cv2.imshow('Frame', frame)
        firstTime = False
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()