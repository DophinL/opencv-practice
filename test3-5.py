"""
图像加权和
"""
import cv2
import numpy as np
a = cv2.imread('./cat.jpeg')
b = cv2.imread('./dog.png')
result = cv2.addWeighted(a, 0.6, b, 0.4, 0)
# result = cv2.add(a, b)
cv2.imshow('test', result)
cv2.waitKey()