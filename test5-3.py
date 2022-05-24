"""
与运算掩模
"""
import cv2
import numpy as np
img = cv2.imread('./cat.jpeg')

img = cv2.resize(img, None, fx=2, fy=1.5)

cv2.imshow('test', img)
cv2.waitKey()
cv2.destroyAllWindows()