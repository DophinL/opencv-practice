"""
与运算掩模
"""
import cv2
import numpy as np
a = cv2.imread('./cat.jpeg')
w, h, c = a.shape
mask = np.zeros((w, h), dtype=np.uint8)
mask[100:200, 200:350] = 255
print(mask[101,201], 'mmmm')
result = cv2.bitwise_and(a, a, mask=mask)
cv2.imshow('test', result)
cv2.waitKey()
cv2.destroyAllWindows()