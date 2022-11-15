import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("Media/Test1_Sample3.jpg", 0)
edges = cv2.Canny(img, 100, 200)

edgesR = cv2.resize(edges, (378, 504))
cv2.imshow("edges", edgesR)
cv2.waitKey(0)
cv2.destroyAllWindows()