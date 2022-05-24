"""
与运算掩模
"""
import cv2
import numpy as np
a = cv2.imread('./shapes.png')

result = cv2.inRange(a, np.array([82-10, 143-10,70-10]), np.array([82+10,143+10,70+10]))

# print(result[100])

a = cv2.bitwise_and(a, a, mask=result)
bgra = cv2.cvtColor(result, cv2.COLOR_GRAY2BGRA)

print(bgra)

cv2.imshow('test', a)
cv2.waitKey()
cv2.destroyAllWindows()