import cv2
import numpy as np
from matplotlib import pyplot as plt
import csv

vid = cv2.VideoCapture("Media/Test2.mp4")
dataFile = open("Calculated_Data/Test2.csv", "w", newline='')
writer = csv.writer(dataFile)
frameCount = 0
firstEnteredFrame = 0
stillInFrame = False
pastXCenter = 0
pastYCenter = 0

while (vid.isOpened()):
    try:
        ret, frame = vid.read()
        frame = cv2.resize(frame, (270, 480), fx = 0, fy = 0, interpolation = cv2.INTER_CUBIC)
        originalWidth = frame.shape[1]
        originalHeight = frame.shape[0]
        x1 = int(originalWidth*(68/128))
        x2 = int(originalWidth*(70/128))
        y1 = int(originalHeight*(4/8))
        y2 = int(originalHeight*(5/8))

        cropped_frame = frame[y1:y2, x1:x2]
        monoColor = cv2.cvtColor(cropped_frame, cv2.COLOR_BGR2GRAY)

        ret, thresh = cv2.threshold(monoColor, 110, 255, cv2.THRESH_BINARY)
        white = np.nonzero(thresh)
        try:
            if (len(white) != 0):
                xCenter = min(white[1])
                pastXCenter = xCenter
                yCenter = white[0][0]
                pastYCenter = yCenter
                if (firstEnteredFrame == 0):
                    print("first time")
                    firstEnteredFrame = 1
                if (firstEnteredFrame == 2):
                    print("second time")
                    cv2.circle(monoColor, (pastXCenter, pastYCenter), 2, (255, 255, 255), -1)
                    cv2.imshow('Frame', frame)
                    cv2.imshow('New_Frame', monoColor)
                    print("Center: "+str(xCenter)+" , "+str(yCenter))
                    writer.writerow([str(xCenter),str(yCenter)])
        except:
            if (firstEnteredFrame == 1):
                firstEnteredFrame = 2
            continue        
        
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    except:
        break

print("Frame count: "+str(frameCount))
writer.writerow([str(frameCount)])
dataFile.close()

vid.release()
cv2.destroyAllWindows()