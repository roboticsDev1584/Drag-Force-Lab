import cv2
import numpy as np
from matplotlib import pyplot as plt
import csv

vid = cv2.VideoCapture("Media/Test7.mp4")
dataFile = open("Calculated_Data/Test7.csv", "w", newline='')
writer = csv.writer(dataFile)
frameCount = 0
firstEnteredFrame = 0
stillInFrame = False
pastXCenter = 0
pastYCenter = 0

while (vid.isOpened()):
    try:
        ret, frame = vid.read()
        #frame = cv2.resize(frame, (270, 480), fx = 0, fy = 0, interpolation = cv2.INTER_CUBIC)
        frame = cv2.resize(frame, (6750, 12000), fx = 0, fy = 0, interpolation = cv2.INTER_CUBIC)
        originalWidth = frame.shape[1]
        originalHeight = frame.shape[0]
        x1 = int(originalWidth*(78/128))
        x2 = int(originalWidth*(82/128))
        y1 = int(originalHeight*(74/128))
        y2 = int(originalHeight*(80/128))

        cropped_frame = frame[y1:y2, x1:x2]
        monoColor = cv2.cvtColor(cropped_frame, cv2.COLOR_BGR2GRAY)
        
        x12 = int(originalWidth*(10/128))
        x22 = int(originalWidth*(50/128))
        y12 = int(originalHeight*(66/128))
        y22 = int(originalHeight*(76/128))
        time_frame = frame[y12:y22, x12:x22]
        
        ret, thresh = cv2.threshold(monoColor, 110, 255, cv2.THRESH_BINARY)
        white = np.nonzero(thresh)
        try:
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
                #cv2.imshow('Time_Frame', time_frame)
                frameCount += 1
                writer.writerow([str(xCenter),str(yCenter)])
                print("Center: "+str(xCenter)+" , "+str(yCenter))
                #cv2.waitKey(1000)
                '''if (frameCount >= 6):
                    cv2.waitKey(1000)'''
        except:
            if (firstEnteredFrame == 1):
                firstEnteredFrame = 2
            '''elif (firstEnteredFrame == 2):
                firstEnteredFrame = 3
            elif (firstEnteredFrame == 3):
                firstEnteredFrame = 4
            elif (firstEnteredFrame == 4):
                firstEnteredFrame = 5'''
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