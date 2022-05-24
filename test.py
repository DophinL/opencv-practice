import cv2
import numpy as np
img = cv2.imread('./calculator.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
t, rst = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
print(t, rst)
cv2.imshow('test', rst)
cv2.waitKey()