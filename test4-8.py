"""
与运算掩模
"""
import cv2
import numpy as np
img = cv2.imread('./cat.jpeg')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)
# adder = np.copy(v)
# adder[:, :] = 20
# print(v)
final = cv2.add(v, 100)
# s += 50
hsv = cv2.merge([h, s, final])
print(v)
img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

cv2.imshow('test', img)
cv2.waitKey()
cv2.destroyAllWindows()