"""
整体提亮、减暗
"""
import cv2
import numpy as np
a = cv2.imread('./cat.jpeg')
lighter = np.ones(a.shape, dtype=np.uint8) * 100
result = cv2.subtract(a, lighter)
cv2.imshow('test', result)
cv2.waitKey()
cv2.destroyAllWindows()