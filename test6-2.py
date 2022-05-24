import cv2
import numpy as np
img = cv2.imread('./calculator.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
rst = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 5)
print(rst)
cv2.imshow('test', rst)
cv2.waitKey()