import cv2
import numpy as np
from matplotlib import pyplot as plt

vid = cv2.VideoCapture("Media/Test7.mp4")

while (vid.isOpened()):
    try:
        ret, frame = vid.read()
        frame = cv2.resize(frame, (270, 480), fx = 0, fy = 0, interpolation = cv2.INTER_CUBIC)
        originalWidth = frame.shape[1]
        originalHeight = frame.shape[0]
        x1 = int(originalWidth*(78/128))
        x2 = int(originalWidth*(82/128))
        y1 = int(originalHeight*(74/128))
        y2 = int(originalHeight*(80/128))

        cropped_frame = frame[y1:y2, x1:x2]
        monoColor = cv2.cvtColor(cropped_frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('Frame', frame)
        cv2.imshow('New_Frame', monoColor)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    except:
        break

vid.release()
cv2.destroyAllWindows()