import cv2
import numpy as np
from matplotlib import pyplot as plt
from datetime import datetime
import csv

vid = cv2.VideoCapture("Media/Test1.mp4")
dataFile = open("Calculated_Data/Test1.csv", "w", newline='')
writer = csv.writer(dataFile)
#avgTimeDelay = 0.0
frameCount = 0
enteredFrame = False
pastXCenter = 0
pastYCenter = 0

while (vid.isOpened()):
    try:
        #currentTime = datetime.now()
        ret, frame = vid.read()
        #scaled frame dimensions: 378x504
        frame = cv2.resize(frame, (756, 1008), fx = 0, fy = 0, interpolation = cv2.INTER_CUBIC)
        frameCount += 1
        originalWidth = frame.shape[1]
        originalHeight = frame.shape[0]
        x1 = int(originalWidth*(68/128))
        x2 = int(originalWidth*(70/128))
        y1 = int(originalHeight*(4/8))
        y2 = int(originalHeight*(5/8))

        cropped_frame = frame[y1:y2, x1:x2]
        frameEdges = cv2.Canny(cropped_frame, 50, 200)

        ret, thresh = cv2.threshold(frameEdges, 127, 255, 0)
        moments = cv2.moments(thresh)
        try:
            xCenter = int(moments["m10"] / moments["m00"])
            pastXCenter = xCenter
            yCenter = int(moments["m01"] / moments["m00"])
            pastYCenter = yCenter
            #this is the first time that it enters the frame
            if (not enteredFrame):
                cv2.circle(frame, (pastXCenter, pastYCenter), 50, (255, 255, 255), -1)
                enteredFrame = True
            cv2.imshow('Frame', frame)
            cv2.imshow('New_Frame', frameEdges)
            print("Center: "+str(xCenter)+" , "+str(yCenter))
        
            writer.writerow([str(xCenter),str(yCenter)])

            #thisTimeDelay = datetime.now() - currentTime
            #print("Time delay: {:.4f}".format(thisTimeDelay.microseconds))
            #avgTimeDelay += thisTimeDelay.microseconds
        except:
            #it entered the cropped video frame previously, but is now gone
            if (enteredFrame):
                cv2.circle(frame, (pastXCenter, pastYCenter), 50, (255, 255, 255), -1)
                cv2.imshow('New_Frame', frameEdges)
            continue
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    except:
        break

#avgTimeDelay /= frameCount
#print("Average time delay: "+"{:.4f}".format(avgTimeDelay))
#writer.writerow(["{:.4f}".format(avgTimeDelay)])
print("Frame count: "+str(frameCount))
writer.writerow([str(frameCount)])
dataFile.close()

#cv2.waitKey(0)
vid.release()
cv2.destroyAllWindows()